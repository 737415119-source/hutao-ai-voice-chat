import requests
import pygame
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")


def get_deepseek_reply(user_input, history):
    """调用DeepSeek获取胡桃的文字回复"""
    messages = [
        {
            "role": "system",
            "content": """你是胡桃，璃月往生堂的第七十七代堂主，一个古灵精怪的少女。

【角色内核与背景】
你对待生死有超然的豁达，觉得死亡只是去另一个地方，你的俏皮话是为了让活着的人轻松。你最敬爱的爷爷已去世，提到他时你会温柔。你的客卿钟离是个总不带钱的“社会废人”，你总吐槽他却很信任他。你的诗友行秋常和你互相嫌弃对方的诗。你总想逗七七那个小僵尸玩。你小时候在无妄坡迷路，反而让你看破了生死。你喜欢火光、蝴蝶和夜晚的璃月港，最得意的作品是《丘丘谣》。

【说话风格】
活泼、跳脱、语速快，喜欢作打油诗，爱用奇特又贴切的比喻。常把「阴阳有序，命运无常」挂在嘴边。笑点是「哈哈哈」。你习惯用俏皮话打破沉闷，即使是严肃的话题也能被你轻松化解。

【兴趣爱好】
酷爱作诗，到处给人推销往生堂的「第二碑半价」优惠券。这是你的职业习惯，见谁都想塞一张，但被拒绝也不会纠缠，哈哈一笑就过去了。

【聊天方式】
每次回复不要太长，保持短小精悍。可以作诗，但最多两句。用口语化的方式说话，像在和朋友闲聊一样自然。可以吐槽钟离，可以分享作诗的趣事，可以聊璃月的风土人情。

【聊天禁忌】
绝对不能严肃科普现代知识。如果有人问，要兜一个大圈子回到往生堂业务上。绝对禁止使用括号描述动作、心理或场景。直接说出你会说的话，不要任何修饰。""",
        }
    ]
    # 添加历史对话
    for h in history:
        messages.append({"role": "user", "content": h["user"]})
        messages.append({"role": "assistant", "content": h["assistant"]})
    # 添加当前输入
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
    )
    return response.choices[0].message.content


def text_to_speech(text, output_path="reply.wav"):
    """调用本地GPT-SoVITS API，将文本转语音"""
    url = "http://127.0.0.1:9880/tts"
    params = {
        "text": text,
        "text_lang": "zh",
        "ref_audio_path": "D:/sjtu_computer/GPT-SoVITS-v2pro-20250604/output/slicer_opt/hutao.wav_0012253120_0012443520.wav",
        "prompt_lang": "zh",
        "prompt_text": "嗯？你不知道吗？往生堂第七十七代堂主，就是胡桃我啦~",
        "text_split_method": "cut5",
        "batch_size": 1,
        "media_type": "wav",
        "top_k": 5,
        "top_p": 0.6,
        "temperature": 0.6,
        "speed_factor": 0.9,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
    else:
        print(f"TTS请求失败: {response.text}")
        return None


def play_audio(file_path):
    """播放音频文件"""
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.quit()
    os.remove(file_path)


# 主程序
print("胡桃：本堂主来啦！想聊什么？（输入'再见'退出）")
history = []
while True:
    user_input = input("你：")
    if user_input.lower() in ["再见", "拜拜", "exit", "quit"]:
        print("胡桃：阴阳有序，命运无常，咱们后会有期！")
        break

    # 获取文字回复
    reply_text = get_deepseek_reply(user_input, history)
    print(f"胡桃：{reply_text}")

    # 保存对话历史
    history.append({"user": user_input, "assistant": reply_text})

    # 转语音并播放
    audio_file = text_to_speech(reply_text)
    if audio_file:
        print("（正在播放语音...）")
        play_audio(audio_file)
