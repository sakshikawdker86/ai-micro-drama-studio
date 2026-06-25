def create_story_prompt(genre, language, audience, duration):

    return f"""
You are a professional micro-drama writer.

Generate a {duration} micro drama.

Genre: {genre}
Language: {language}
Target Audience: {audience}

IMPORTANT:
Return the output using EXACTLY these headings.
Do not rename them.
Do not skip any section.

## Title

## Characters
- Name:
- Age:
- Personality:
- Role:

## Story
Scene 1

Scene 2

Scene 3

Ending

## Thumbnail Prompt

Generate ONE highly detailed cinematic AI image prompt including:
- Character appearance
- Emotion
- Lighting
- Camera angle
- Background
- Ultra realistic
- 4K
- Cinematic

## Voiceover Script

Write an emotional narration (80–120 words) suitable for a 1-minute short video.

## Instagram Caption

Write a catchy Instagram caption in maximum 2 lines with 2–3 emojis.

## Hashtags

Generate exactly 10 hashtags.
"""