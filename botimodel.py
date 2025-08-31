import discord
from discord.ext import commands
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import random
from keras.layers import TFSMLayer
from difflib import get_close_matches
#/////POTRZEBNY TWÓJ WŁASNY MODEL (saved_model) KTÓRY MOŻESZ STWORŻYĆ W GOOGLE TEACHABLE MACHINE LUB W PYTHONIE Z TENSORFLOW//////
# === Discord setup ===
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)

# === Załaduj funkcjonujący model jako TFSMLayer (Keras 3) ===
model = TFSMLayer(r"Twój saved_model jako tfsm keras 3", call_endpoint="serving_default")

# === ładowanie labels=
with open(r"converted_savedmodel\labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

#Kategorie
advice_dict = {
    "Zanieczyszcanie": [
        "🚲 Zamiast jeździć samochodem, spróbuj jeździć rowerem lub korzystać z komunikacji miejskiej.",
        "♻️ Poddawaj recyklingowi i kompostowaniu, aby zmniejszyć ilość odpadów.",
        "🚯 Jeśli to możliwe, unikaj plastików jednorazowego użytku."
    ],
    "Energia odnawialna": [
        "🔋 Gdy tylko możesz, korzystaj z odnawialnych źródeł energii.",
        "💡 Oszczędzaj energię elektryczną wyłączając nieużywane urządzenia.",
        "🌱 Wspieraj politykę czystej energii w swojej społeczności / sąsiedztwie"
    ],
    "topniące lodowce": [
        "🌍 Zmniejsz produkcje co2 jedząc więcej produktów roślinnych lub kupując mięso / inne od ekologicznych rolników.",
        "🧳 Podróżuj eko i unikaj zbędnych lotów, krótkich podróży samochodem itp.",
        "🪵 Wesprzyj grupy ochrony środowiska które chronią regiony polarne przekazywując datki itd."
    ],
    "wylesianie": [
        "🌲 Wspieraj projekty zalesiania lub sadź drzewa lokalnie.",
        "📄 Ogranicz zużycie papieru i korzystaj z rozwiązań dygitalnych kiedykolwiek możliwie.",
        "🥩 Jedz mniej wołowiny / mięsa, aby zmniejszyć zapotrzebowanie na pola."
    ],
    "energia": [
        "⚡ W miarę możliwości przejdź na energię odnawialną (zamontuj panele słoneczne lub znajdź dostawcę energii odnawialnej)."
    ]
}

# Pomaga do predykcji
def predict_image(img_array):
    raw_preds = model(img_array)  # output: list of dicts with tensors
    preds = []

    if isinstance(raw_preds, dict):
        raw_preds = [raw_preds]
    elif not isinstance(raw_preds, (list, tuple)):
        raw_preds = list(raw_preds)

    for item in raw_preds:
        if isinstance(item, dict):
            for key, tensor in item.items():
                probs = tensor.numpy()[0]  # shape (num_classes,)
                max_idx = int(np.argmax(probs))
                class_name = labels[max_idx]
                confidence = float(probs[max_idx])
                preds.append({"class_name": class_name, "confidence": confidence})
        else:
            preds.append({"class_name": "unknown", "confidence": float(item)})

    return preds

# === Events ===
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    channel = bot.get_channel(twójchannelID)  
    if channel:
        await channel.send(f"Cześć, mam na imię {bot.user}")
        await channel.send("Byłem stworzony, żeby pomóc szerzyć świadomość o zmianie klimatu. 🌍")

# === Commands ===
@bot.command()
async def advice(ctx, topic: str):
    topic = topic.lower()
    if topic in advice_dict:
        advice = random.choice(advice_dict[topic])
        await ctx.send(f"💡 Advice for **{topic}**: {advice}")
    else:
        await ctx.send(
            "❓ I don't have advice for that yet. Try: pollution, deforestation, energy, renewable energy, melting glaciers."
        )

@bot.command()
async def predict(ctx):
    if not ctx.message.attachments:
        await ctx.send("⚠️ Załącz jakieś zdjęcie do predykcji")
        return

    img_url = ctx.message.attachments[0].url
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content)).convert("RGB")

    img = img.resize((224, 224))
    img_array = np.array(img).astype(np.float32)
    img_array = (img_array / 127.5) - 1
    img_array = np.expand_dims(img_array, axis=0)

    # Predykcje
    predictions = predict_image(img_array)

    # Do debugowania: Surowe predykcje
    print("Raw predictions:", predictions)

    # Wybierz największą pewność
    best_pred = max(predictions, key=lambda x: x.get("confidence", x.get("score", 0)))
    class_name = best_pred.get("class_name", best_pred.get("label", "unknown")).strip().lower()
    confidence = best_pred.get("confidence", best_pred.get("score", 0.0))

    # Do debugowania: Pokaż imię klasy i kategori rad
    print("Predicted class_name:", class_name)
    print("Advice topics:", list(advice_dict.keys()))

    # Fuzzy match model label to advice topics (more lenient)
    normalized_topics = [t.lower() for t in advice_dict.keys()]
    matched_topic = get_close_matches(class_name, normalized_topics, n=1, cutoff=0.3)
    if matched_topic:
        advice = random.choice(advice_dict[matched_topic[0]])
    else:
        advice = "Nie ma rady na taką klasę!!"

    await ctx.send(
        f"Mysle że twoje zdjęcie reprezentuje: **{class_name}** "
        f"(confidence: {confidence*100:.1f}%).\n💡 Rada: {advice}"
    )

# URUCHOM BOTA!!!!
bot.run("twój_bot_token")

