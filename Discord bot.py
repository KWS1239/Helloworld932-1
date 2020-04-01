import discord
import openpyxl

client = discord.Client()

learned_msg_list = []

G = False

import time

now = time.localtime()

import random

#봇 가동
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("와니야 자기소개")


@client.event
async def on_message(message): #채팅 명령어에 따른 결과
    chat_msg = message.content
    if chat_msg.startswith("와니야 안녕"):
        await message.channel.send("안녕!!!!")
    elif chat_msg.startswith("와니야 초대링크") and chat_msg.endswith("와니야 초대링크"):
        await message.channel.send("여기로 초대 가능해요")
        await message.channel.send("https://discordapp.com/oauth2/authorize?client_id=688556864291864636&permissions=8&scope=bot ")

    elif chat_msg.startswith("와니야 인사"):
        await message.channel.send("반갑습니다!")
    elif chat_msg.startswith("와니야 ㅎㅇ"):
        await message.channel.send("안녕하세욧!!")
    elif chat_msg.startswith("와니야 뒤져"):
        await message.channel.send("켁.")
    elif chat_msg.startswith("와니야 잘가"):
        await message.channel.send("먼저 가세요!")
    elif chat_msg.startswith("와니야 잘가"):
        await message.channel.send("빠이빠이!!")
    elif chat_msg.startswith("와니야 안녕하살법"):
        await message.channel.send("안녕하살법 받아치기! 퍽! 으아 머리가 아파요")
    elif chat_msg.startswith("와니야 하이루"):
        await message.channel.send("하이")
    elif chat_msg.startswith("와니야 고마워"):
        await message.channel.send("고맙긴요!")
    elif chat_msg.startswith("와니야") and chat_msg.endswith("좋아해?"):
        await message.channel.send('당근이죠!')
    elif chat_msg.startswith("와니야") and chat_msg.endswith("ㅇㅋ?"):
        await message.channel.send("ㅇㅋ!")
    elif chat_msg.startswith("와니야") and chat_msg.endswith("알아?"):
        await message.channel.send("전 바보라 몰라요!")
    elif chat_msg.startswith("와니야 뭐해"):
        await message.channel.send("아무것도 안 하고 있어요...")

    elif chat_msg.startswith("와니야") and chat_msg.endswith("와니야"):
        await message.channel.send("?")
    elif chat_msg.startswith("와니야") and chat_msg.endswith("하자"):
        await message.channel.send('안할거임 ㅅㄱ')
    elif chat_msg.startswith("와니야") and chat_msg.endswith("하자니까"):
        await message.channel.send("안한다고 임마")
    elif chat_msg.startswith("와니야 도배") and chat_msg.endswith("와니야 도배"):
        await message.channel.send("너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이"
                                   "너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이"
                                   "너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이"
                                   "너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이"
                                   "너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이"
                                   "너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이너희들멍청이")
    elif chat_msg.startswith("와니야 잠자") and chat_msg.endswith("와니야 잠자"):
        await client.change_presence(status=discord.Status.offline)
    elif chat_msg.startswith("와니야 깨") and chat_msg.endswith("와니야 깨"):
        await client.change_presence(status=discord.Status.online)
        game = discord.Game("와니야 시간")
    elif chat_msg.startswith("와니야 왜"):
        await message.channel.send("그러게요 왜 그럴까요?")
    elif chat_msg.startswith("와니야") and chat_msg.endswith("해줘"):
        await message.channel.send("아 다 귀찮아서 하기 시름")
    elif chat_msg.startswith("와니야 넌") and chat_msg.endswith("해"):
        await message.channel.send("고마워요!!! 그리고 사실 전 나쁘다고 해도 좋아욧")
    elif chat_msg.startswith("와니야 너가") and chat_msg.endswith("된다며"):
        await message.channel.send("언제 그랬지??? 기억이 안나네")
    elif chat_msg.startswith("와니야 와리"):
        await message.channel.send("나 만든 사람인가??ㅎ")
    elif chat_msg.startswith("와니야") and chat_msg.endswith("?"):
        yesorno = ["네!!","아니요!!"]
        await message.channel.send(random.choice(yesorno))
    elif chat_msg.startswith("와니야 업그레이드") and chat_msg.endswith("와니야 업그레이드"):
        G = True
        level=0
        while True:
            if G == True:
                level = level + 1
                await message.channel.send("파워 업그레이드 중 입니다.10초 뒤에 레벨이 올라갑니다")
                time.sleep(10)
                await message.channel.send("파워 업그레이드 중. 현재"+str(level)+'레벨 입니다.')
                if level == 5:
                    await message.channel.send("현재 '물'등급 입니다")
                elif level == 10:
                    await message.channel.send("현재 '아이스' 등급 입니다")
                elif level == 20:
                    await message.channel.send("현재 '프리 일렉트로'등급 입니다")
                elif level == 30:
                    await message.channel.send("현재 '메가 일렉트로'등급 입니다")
                elif level == 40:
                    await message.channel.send("현재 '울트라 일렉트로'등급 입니다")
                elif level == 50:
                    await message.channel.send("만렙 달성!! 현재 '마스터 에이스 흑당 버블티 피자 치킨햄버거' 등급입니다!")
                    break
    elif chat_msg.startswith("와니야 자기소개") and chat_msg.endswith("와니야 자기소개"):
        await message.channel.send("내 이름은 와니봇 v2이지! 난 예전에 그냥 와니봇이였지만 업그레이드 되어 돌아왔다! 명령어도 쓸 수 있다!")
        await message.channel.send("```와니야 안녕```")
        await message.channel.send("```와니야 공격 [타겟 이름]```")
        await message.channel.send("```와니야 보스전 [무기이름]```")
        await message.channel.send("```와니야 업그레이드```")

        await message.channel.send("```와니야 {기쁨, 화남, 흥분, 웃어, 귀요미, 슬픔}```")
        await message.channel.send("```와니야 초대링크```")
        await message.channel.send("등등 많이 있음")
    elif chat_msg.startswith("와니야 바이"):
        await message.channel.send("빠이빠이!!")
    elif chat_msg.startswith("와니야 ㅂㅇ"):
        await message.channel.send("ㅂㅂ")
    elif chat_msg.startswith("와니야 심영"):
        await message.channel.send("야인시대에서 내가 고자라니라고 한사람 맞죠?")
    elif chat_msg.startswith("와니야 호구마"):
        await message.channel.send("호구마요?ㅋㅋㅋㅋㅋㅋ 호~박~고구마죠~ㅋㅋ")
    elif chat_msg.startswith("와니야 내가 고자라니"):
        await message.channel.send("안되겠오..쏩시다!")
    elif chat_msg.startswith("와니야 아잇"):
        await message.channel.send("응! 아잇! 풀을으 12번?")
    elif chat_msg.startswith("와니야 코로나바이러스"):
        await message.channel.send("마스크 안 쓰면 서버에서 벤 당한다는 그 바이러스 맞죠? 와리 형이 가르쳐줬어요")
    elif chat_msg.startswith("와니야 아임뚜렛"):
        await message.channel.send("응! 아잇! 풀을으 12번?")
    elif chat_msg.startswith("와니야 폭"):
        await message.channel.send("펑! :exploding_head: ")
    elif chat_msg.startswith("와니야 김두한"):
        await message.channel.send("함께 폭4하자.")
    elif chat_msg.startswith("와니야 죽어"):
        await message.channel.send("(대충 죽어있다는 말)")
    elif chat_msg.startswith("와니야 보스전") and chat_msg.endswith("와니야 보스전"):
        await message.channel.send("올바른 사용법 : 와니야 보스전 [무기 이름]")
    elif chat_msg.startswith("와니야 보스전"):
        result = ['보스전에서 승리했습니다!!','좋지 않은 확률로 졌습니다. 다시 시도 ㄱㄱ']
        bossAttack = ['칼','면도기','기관총','회전회오리','자신의 몸을 던지는 방법','빡빡이','심영','빌딩','모티스의 박쥐','자신의 방귀냄새']
        keyword = chat_msg[8:]

        await message.channel.send(keyword+" 무기를 사용하셨습니다.")
        time.sleep(5)
        await message.channel.send("보스가 "+random.choice(bossAttack)+"(으)로 공격하였습니다.")


        await message.channel.send(random.choice(result))
    elif chat_msg.startswith("와니야 귀요미"):
        await message.channel.send("이거요")
        await message.channel.send("https://tenor.com/view/bye-slide-baby-later-peace-out-gif-12999722")
    elif chat_msg.startswith("와니야 화남"):
        await message.channel.send("이거 맞죠")
        await message.channel.send("https://tenor.com/view/angry-mad-nope-gif-10535329")
    elif chat_msg.startswith("와니야 공격"):
        Atkmeme = ['https://tenor.com/view/freaking-out-kermit-gif-8832122',
                   'https://tenor.com/view/dragon-ball-z-goku-super-saiyan-against-android-13-gif-12485392' ]
        target = chat_msg[7:]
        await message.channel.send(target+ " 내 주먹을 맞아라! 무다무다무다무다무다무다무다무다!!!ㅋㅋㅋㅋㅋㅋㅋ")
        await message.channel.send(random.choice(Atkmeme))
    elif chat_msg.startswith("와니야 흥분"):
        await message.channel.send("흥분한드아아아아아")
        await message.channel.send("https://tenor.com/view/jonah-hill-yay-greek-aldos-gif-7212866")
    elif chat_msg.startswith("와니야 웃어"):
        await message.channel.send("웃어야지 하하핳")
        await message.channel.send("https://tenor.com/view/seo-eunkwang-bto-b-kpop-korean-laugh-gif-9852675")
    elif chat_msg.startswith("와니야 기쁨"):
        nicememe = ["https://tenor.com/view/funny-dance-hilarious-likewhatdance-gif-5784899",
                    "https://tenor.com/view/dancing-gif-9878005","https://tenor.com/view/dancing-dance-gif-10208597"]
        await message.channel.send("기쁩니다!")
        await message.channel.send(random.choice(nicememe))
    elif chat_msg.startswith("와니야 슬픔"):
        sadmeme = ["https://tenor.com/view/baby-crying-gif-5943705","https://tenor.com/view/pensiveface-gif-4425081"]
        await message.channel.send("ㅠㅠ")
        await message.channel.send(random.choice(sadmeme))

    elif chat_msg.startswith("와니야"):
        await message.channel.send("넹?")








client.run("Njg4NTU2ODY0MjkxODY0NjM2.Xm2LlA.3VHriKhL4Ng9qOfuC8kqBwNhWD0")