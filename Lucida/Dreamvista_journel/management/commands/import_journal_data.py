# your_app_name/management/commands/import_journal_data.py
from django.core.management.base import BaseCommand
from Dreamvista_journel.models import journel
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Import data into journel model'

    def handle(self, *args, **options):
        # Your data entry logic here
        dream_stories = [
            "I walked through a forest of sparkling crystals, each tree emitting a soft glow. The ground beneath me felt like a bed of velvet, and the air was filled with the scent of stardust.",
            "In a surreal underwater city, I conversed with wise sea creatures who shared tales of forgotten civilizations. The coral buildings shimmered in a mesmerizing display of bioluminescence.",
            "A giant floating balloon carried me across a sky painted in vibrant hues. As I looked down, I saw islands in the shape of animals, forming a magical archipelago in the clouds.",
            "I discovered a hidden cave filled with glowing mushrooms that emitted musical notes when touched. The cavern echoed with a symphony of enchanting sounds, creating a harmony of nature.",
            "I rode a majestic phoenix through the cosmos, passing by celestial bodies and witnessing the birth of galaxies. The universe unfolded before my eyes in a breathtaking cosmic journey.",
            "A door in the middle of a meadow transported me to a library where each book contained the essence of a different emotion. Reading them allowed me to experience the stories as vividly as the characters.",
            "I found myself in a city of mirrors, reflecting infinite versions of myself. Each reflection had a unique story, and together, we explored the endless possibilities of existence.",
            "A time-traveling train carried me through historical epochs. I conversed with historical figures, witnessing pivotal moments in time and gaining insights into the interconnectedness of the past and present.",
            "I navigated a dreamlike maze of floating islands, each with its own ecosystem. Mythical creatures guided me, and the landscape transformed with my emotions, reflecting the inner workings of my mind.",
            "In a garden where flowers bloomed based on emotions, I discovered a rare blossom representing gratitude. As I expressed gratitude, the flower unfolded into a portal, revealing a hidden realm of tranquility.",
            "I sailed across a sea of dreams in a boat made of moonlight. The constellations above whispered ancient stories, and shooting stars illuminated the path, guiding me to ethereal realms.",
            "I became a character in a living painting, exploring landscapes that transformed with each brushstroke. The artist, a cosmic entity, painted the canvas of reality, and I witnessed the creation of worlds.",
            "I danced with fireflies in a magical forest, and their glow created patterns in the air. The trees whispered secrets, and the fireflies carried my wishes to the stars, turning them into constellations.",
            "I walked on clouds in a sky filled with floating islands. Each island had its own ecosystem, and mythical creatures inhabited them. As I explored, the clouds transformed into cotton candy, creating a sweet atmosphere.",
            "I entered a dimension of floating bubbles, each containing a different reality. Popping a bubble revealed a snapshot of a moment in time, and I witnessed the kaleidoscope of experiences within the multiverse.",
            "I attended a celestial masquerade ball on the moon, where cosmic beings wore masks of galaxies. The dance floor reflected the cosmos, and each step created ripples of stardust.",
            "I befriended talking constellations that shared stories of the universe. Together, we created a cosmic tapestry, weaving the threads of destiny and witnessing the interconnectedness of all things.",
            "I climbed a staircase made of rainbows, reaching a realm where colors had personalities. Each hue told stories of its origin, and together, they painted the canvas of existence with vibrant tales.",
            "I explored a city made of dreams, where buildings were shaped like thoughts. Walking through the streets allowed me to enter the minds of the dreamers, experiencing their aspirations and fears.",
            "I discovered a gateway to the upside-down world, where gravity worked in reverse. Floating landscapes and upside-down creatures created a surreal environment, challenging my perception of reality.",
        ]

        # Manually generated titles
        titles = [
            "Crystal Whispers",
            "City of Bioluminescence",
            "Skyborne Archipelago",
            "Mushroom Symphony",
            "Cosmic Phoenix Journey",
            "Emotional Library Portal",
            "Infinite Reflections",
            "Epochs on the Time Train",
            "Mythical Maze Odyssey",
            "Garden of Gratitude",
            "Moonlit Sea Voyage",
            "Living Painting Chronicles",
            "Firefly Dance",
            "Cloud Candy Wonderland",
            "Bubble Dimension Snapshots",
            "Celestial Masquerade",
            "Constellation Conversations",
            "Rainbow Staircase Reverie",
            "City of Thoughtful Buildings",
            "Upside-Down Gateway",
        ]

        # Starting date for entries
        current_date = date(2023,10,20)

        # List to store the data
        data_to_insert = []

        # Generating data for each dream story
        for title, story in zip(titles, dream_stories):
            data_to_insert.append({
                'date': current_date,
                'title': title,
                'experience': story,
            })

            # Incrementing date for the next entry
            current_date += timedelta(days=1)

        # Using bulk_create for better performance
        journel.objects.bulk_create([journel(**data) for data in data_to_insert])

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
