def create_story_prompt(genre, language, audience, duration):

    return f"""
You are a professional micro-drama writer.

Generate a {duration} micro drama.

Genre: {genre}

Language: {language}

Target Audience: {audience}

Return:

Title

Characters

Scene 1

Scene 2

Scene 3

Ending
"""