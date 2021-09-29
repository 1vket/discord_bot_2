import datetime
from func.util import chaimu
import asyncio

# -P or -pomodoro で実行
# -P [clock num]
async def pomodoro(message, vc=None) -> None:

    # clock を設定
    try:
        clock = int(message.content.split()[1])
    except IndexError:
        clock = 1

    nextTime = datetime.datetime.now()

    i = 0
    qk = True

    while 1:
        if datetime.datetime.now() > nextTime:
            if qk:
                nextTime = datetime.datetime.now() + datetime.timedelta(minutes=25)
                qk = False
                await chaimu(message, vc)
                await message.channel.send('--focus!!--' + datetime.datetime.now().strftime('(%m-%d %H:%M') +" ~ "+ nextTime.strftime('%H:%M)')  + '\n頑張ってね')
                i += 1
            else:
                # 終了フラグ
                if i >= clock:
                    break
                qk = True
                await chaimu(message, vc)
                
                # 4回ごとの休憩
                if i%4 == 0:
                    nextTime = datetime.datetime.now() + datetime.timedelta(minutes=15)
                    await message.channel.send('--break time!!--' + datetime.datetime.now().strftime('(%m-%d %H:%M') +" ~ "+ nextTime.strftime('%H:%M)')  + '\n15分休憩だよ')
                else:
                    nextTime = datetime.datetime.now() + datetime.timedelta(minutes=5)
                    await message.channel.send('--break time!!--' + datetime.datetime.now().strftime('(%m-%d %H:%M') +" ~ "+ nextTime.strftime('%H:%M)')  + '\n 5分休憩だよ')

        await asyncio.sleep(1)
    await message.channel.send('----FINISH!!----\nがんばったね！おつかれさま♪')