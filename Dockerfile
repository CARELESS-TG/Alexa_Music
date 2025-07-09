# ⚙️ Base image with Python 3.10 and Node.js 19
FROM nikolaik/python-nodejs:python3.10-nodejs19

# 🔧 Install ffmpeg (for audio streaming)
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 📂 Copy all project files into /app/
COPY . /app/
WORKDIR /app/

# 📦 Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# 🚀 Start the bot
CMD ["bash", "start"]
