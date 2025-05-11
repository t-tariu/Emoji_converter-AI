from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def convert_to_emoji(text):
    system_prompt = (
        "너는 사용자 문장을 간결하고 적절한 이모지 시퀀스로 번역하는 AI야. "
        "가능한 텍스트 없이 이모지만 출력해. 감정, 상황, 동작을 고려해서 자연스럽게 번역해."
        "예: '오늘 시험 망했어' → 😩📉📚"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.7,
            max_tokens=60
        )
        emoji_output = response.choices[0].message.content.strip()
        return emoji_output
    except Exception as e:
        return f"⚠️ 오류 발생: {str(e)}"
