def create_story_prompt(genre, language, audience, duration):

    return f"""
You are a professional micro-drama writer.

Generate a {duration} micro drama.

Genre: {genre}

Language: {language}

Target Audience: {audience}

Return:

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

Write one highly detailed cinematic AI image prompt.

The prompt should include:
- Character appearance
- Emotion
- Lighting
- Camera angle
- Background
- Ultra realistic
- 4K
- Cinematic

## Voiceover Script

Write a cinematic voiceover narration for the story.

Requirements:
- Emotional tone
- 80–120 words
- Suitable for a 1-minute short video
- End with a hook that keeps viewers engaged.



"""

