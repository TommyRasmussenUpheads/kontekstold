from flask import Flask, render_template_string

app = Flask(__name__)

# Her kan du enkelt legge til nye bloggposter og videolenker senere
DATA = {
    "title": "Kontekst - Min AI Reise",
    "description": "Her samler jeg mine tanker, videoer og erfaringer rundt AI-utvikling og autonome agenter.",
    "videos": [
        {
            "title": "Min første AI Video på LinkedIn",
            "url": "https://www.linkedin.com",  # Bytt ut med faktisk link eller embed senere
            "desc": "En introduksjon til hvordan jeg gikk fra 0 koding til container-drifting."
        }
    ],
    "blogs": [
        {
            "title": "Hvorfor jeg bygger på min egen server",
            "date": "Mai 2026",
            "content": "Å ha full kontroll på infrastrukturen er kritisk for å forstå hvordan autonome agenter samhandler med omverdenen..."
        }
    ]
}

@app.route('/')
def home():
    # Enkel, ren HTML med Tailwind CSS for pent design
    html_template = """
    <!DOCTYPE html>
    <html lang="no">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ data.title }}</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-900 text-gray-100 font-sans antialiased">
        <div class="max-w-4xl mx-auto px-4 py-12">
            <!-- Header -->
            <header class="mb-16 border-b border-gray-800 pb-8">
                <h1 class="text-4xl font-extrabold tracking-tight text-white mb-4">kontekst.skydotten.no</h1>
                <p class="text-xl text-gray-400">{{ data.description }}</p>
            </header>

            <!-- Video Seksjon -->
            <section class="mb-16">
                <h2 class="text-2xl font-bold text-blue-400 mb-6">Siste Videoer</h2>
                <div class="grid gap-6">
                    {% for video in data.videos %}
                    <div class="bg-gray-800 p-6 rounded-lg border border-gray-700">
                        <h3 class="text-xl font-semibold mb-2">{{ video.title }}</h3>
                        <p class="text-gray-400 mb-4">{{ video.desc }}</p>
                        <a href="{{ video.url }}" target="_blank" class="text-blue-400 hover:underline">Se på LinkedIn &rarr;</a>
                    </div>
                    {% endfor %}
                </div>
            </section>

            <!-- Blogg Seksjon -->
            <section>
                <h2 class="text-2xl font-bold text-green-400 mb-6">Bloggposter & Tanker</h2>
                <div class="grid gap-8">
                    {% for post in data.blogs %}
                    <article class="bg-gray-800 p-6 rounded-lg border border-gray-700">
                        <span class="text-sm text-gray-500">{{ post.date }}</span>
                        <h3 class="text-xl font-semibold my-2">{{ post.title }}</h3>
                        <p class="text-gray-300 leading-relaxed">{{ post.content }}</p>
                    </article>
                    {% endfor %}
                </div>
            </section>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, data=DATA)

if __name__ == '__main__':
    # Setter porten til 3020 slik du ønsket
    app.run(host='0.0.0.0', port=3020)
