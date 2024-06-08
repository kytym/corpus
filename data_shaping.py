import re

def main():
    f = open("ningen_shikkaku.txt", "r", encoding="utf-8")
    data = f.read()
    f.close()

    f = open("test.txt", "w", encoding="utf-8")
    f.write(shaping(data))
    f.close()

#データの加工
def shaping(data):
    #改行の削除
    shaped = re.sub("\u3000","",data)
    #<<>>のルビの削除
    shaped = re.sub("《[^》]+》", "", shaped)
    #文頭、文末の削除
    shaped = re.sub("人間失格\n太宰治\n\n-------------------------------------------------------\n【テキスト中に現れる記号について】\n\n《》：ルビ\n（例）従姉妹\n\n｜：ルビの付く文字列の始まりを特定する記号\n（例）昔｜気質\n\n［＃］：入力者注主に外字の説明や、傍点の位置の指定\n（例）［＃３字下げ］はしがき［＃「はしがき」は大見出し］\n-------------------------------------------------------\n\n","",shaped)
    shaped = re.sub("\n\n\n\n底本：「人間失格」新潮文庫、新潮社\n1952（昭和27）年10月30日発行\n1985（昭和60）年１月30日100刷改版\n初出：「展望」筑摩書房\n1948年（昭和23年）6〜8月号\n入力：細渕真弓\n校正：八巻美惠\n1999年1月1日公開\n2011年1月9日修正\n青空文庫作成ファイル：\nこのファイルは、インターネットの図書館、青空文庫（http://www.aozora.gr.jp/）で作られました。入力、校正、制作にあたったのは、ボランティアの皆さんです。\n","", shaped)
    shaped = re.sub("［＃改頁］","", shaped)

    return shaped

if __name__ == "__main__":  
    main()