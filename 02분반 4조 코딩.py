line ='─'*70
key1 = '(미)'
key2 = '(종)'
key3 = '(유)'
key4 = '(의)'

def qz1():
      answer = input('답을 말해보거라 : ')
      if answer == 'O' or answer == 'o' :
        print("")
        print("")
        print("문지기1 : 통과해도 좋다. 석조전은 대표적인 유럽풍의 석조 건축물로, 1910년 중공된 궁중건물입니다. ")
        print('          황제께서는 고관대신들과 외국 사절을 만나는 용도로 이곳을 사용하시고 있습니다. ')
        print("")
        print('해설: 유엔 한국위원단이 이곳을 사무실로 사용하였다. ')
        print('      국립중앙박물관, 궁중유물전시관 등으로 사용되기도 하였다. ')
        print('      2014년에 석조전 대한제국역사관으로 개관하였다.')
        print("")
        print("문지기1 : 다음 건물로 넘어가라. 탈출에 필요한 키워드는 (미) 이다. ")
        qz2()
      else:
        answer = input('문지기1 : 틀렸다. 기회를 한 번 더 주겠다. : ')
        if answer == 'O' or answer == 'o' :
          print("")
          print("")
          print('문지기1 : 통과해도 좋다. 석조전은 대표적인 유럽풍의 석조 건축물로, 1910년 중공된 궁중건물입니다. ')
          print('          황제께서는 고관대신들과 외국 사절을 만나는 용도로 이곳을 사용하고 계시다. ')
          print("")
          print('해설: 유엔 한국위원단이 이곳을 사무실로 사용하였다.')
          print('      국립중앙박물관, 궁중유물전시관 등으로 사용되기도 하였다. ')
          print('      2014년에 석조전 대한제국역사관으로 개관하였다.')
          print("")
          print("문지기1 : 다음 건물로 넘어가라. 탈출에 필요한 키워드는 (미) 이다. ")
          qz2()
          print("")
        else:
          print("")
          print("")
          print('문지기1 : 틀렸다. 널 감옥에 가두겠다!')
          print("")
          print('해설: 석조전은 대표적인 유럽풍의 석조 건축물로, 1910년 중공된 궁중건물입니다. ')
          print('      황제께서는 고관대신들과 외국 사절을 만나는 용도로 이곳을 사용하고 계시다. ')
          print("")
          print("      유엔 한국위원단이 이곳을 사무실로 사용하였다. ")
          print('      국립중앙박물관, 궁중유물전시관 등으로 사용되기도 하였다. ')
          print('      2014년에 석조전 대한제국역사관으로 개관하였다. 알아두거라!')
          print("")
          print('『게임종료』')
        print(line)


def qz2():
    print("")
    print(line)
    print("당신은 석조전에서 나와 주변을 살펴보던 중 다음 건물로 들어갔다.")
    print("")
    print("")
    print("병사 : 자네가 있는 이곳은 정관헌이다! 우리 고종 황제께서는 어떤 음료를 즐겨 마셨도다. 보기를 보고 번호를 써라!")
    print("")
    print("")
    print("병사 : 1, 콜라/ 2. 커피/ 3. 홍차/ 4. 식혜/ 5. 우유")
    print("")
    print("")
    answer=input("병사 : 얼른 대답해보거라! : ")
    if answer == '2' :
        print("정답이다!")
        print("")
        print('병사 : 정관헌은 조선 역대 왕의 초상화인 어진을 봉안했던 장소로 약 1900년 건립되었다. ')
        print("")
        print('       이 전각은 동서양의 양식을 모두 갖춘 건물로 지붕은 팔작지붕으로 동양식이다.')
        print("")
        print('       건물은 차양칸과 난간을 서양식처럼 꾸몄다.')
        print("")
        print('병사 : 다음 건물로 넘어가라. 탈출에 필요한 키워드는 (종) 이다.')
        qz3()
    else:
        answer = input("병사 : 틀렸다. 기회를 한번 더 주겠다. :")
        if answer == '2':
            print("병사 : 정답이다!")
            print("")
            print('병사 : 정관헌은 조선 역대 왕의 초상화인 어진을 봉안했던 장소로 약 1900년 건립되었다. ')
            print("")
            print('       이 전각은 동서양의 양식을 모두 갖춘 건물로 지붕은 팔작지붕으로 동양식이다.')
            print("")
            print('       건물은 차양칸과 난간을 서양식처럼 꾸몄다.')
            print("")
            print('병사 : 다음 건물로 넘어가라. 탈출에 필요한 키워드는 (종) 이다.')
            qz3()
        else:
            print("병사 : 틀렸다. 정답은 2번 커피다. 널 감옥에 가두겠다.")
            print('병사 : 정관헌은 조선 역대 왕의 초상화인 어진을 봉안했던 장소로 약 1900년 건립되었다. ')
            print("")
            print('       이 전각은 동서양의 양식을 모두 갖춘 건물로 지붕은 팔작지붕으로 동양식이다.')
            print("")
            print('       건물은 차양칸과 난간을 서양식처럼 꾸몄다. 알아두거라!')
            print("")
            print("『게임종료』")

def qz3() :
    print("")
    print(line)
    print("당신은 정관헌에서 나와 주변에 보이는 다음 건물로 들어갔다.")
    print("")
    print("")
    print("문지기2 : 이곳은 석어당이다! 다음문제를 보고 알맞은 답을 말해라!")
    print("")
    print("")
    print('문지기2: 조선의 왕 선조는 1592년에 일어난 0000으로 인해 의주로 피난을 갔다.')
    print('         0000은 무엇인가?')
    print("")
    print("")
    answer=input("병사 : 얼른 대답해보거라! : ")
    if answer == '임진왜란' :
        print("정답이다!")
        print("")
        print('문지기2: 선대 왕이신 선조께서 왜놈들이 쳐들어 오는 바람에 피난을 갔다 오시고 여기에 머무셨지...')
        print("")
        print('         그리고 광해군이 이복형제의 어머니 인목왕후를 위폐시킨 곳이기도 해.')
        print("")
        print('         후에는 인조반정이 일어나서 광해군의 죄를 문책한 곳이지..')
        print("")
        print('문지기2: 다음 건물로 넘어가라. 탈출에 필요한 키워드는 (유) 이다.')
        qz4()
    else:
        answer = input("병사 : 틀렸다. 기회를 한번 더 주겠다. :")
        if answer == '임진왜란':
            print(" 병사 : 정답이다!")
            print("")
            print('문지기2: 선대 왕이신 선조께서 왜놈들이 쳐들어 오는 바람에 피난을 갔다 오시고 여기에 머무셨지...')
            print("")
            print('         그리고 광해군이 이복형제의 어머니 인목왕후를 위폐시킨 곳이기도 해.')
            print("")
            print('         후에는 인조반정이 일어나서 광해군의 죄를 문책한 곳이지..')
            print("")
            print('문지기2: 다음 건물로 넘어가라. 탈출에 필요한 키워드는 (유) 이다.')
            qz4()
        else:
            print("병사 : 틀렸다. 정답은 임진왜란이다. 널 감옥에 가두겠다.")
            print("")
            print('문지기2: 선대 왕이신 선조께서 왜놈들이 쳐들어 오는 바람에 피난을 갔다 오시고 여기에 머무셨지...')
            print("")
            print('         그리고 광해군이 이복형제의 어머니 인목왕후를 위폐시킨 곳이기도 해.')
            print("")
            print('         후에는 인조반정이 일어나서 광해군의 죄를 문책한 곳이지. 알아두거라!')
            print("")
            print("『게임종료』")

def qz4() :
     print("")
     print(line)
     print("당신은 석어당에서 나와 마지막 건물로 들어갔다.")
     print("")
     print("")
     print("병사2 : 이곳은 중명전이다! 다음 문제를 보고 알맞는 답을 적어라.")
     print("")
     print("")
     print("병사2 : 중면전에서 1905년 대한제국의 외교권을 빼앗긴 조약을 체결했다.")
     print('        조약의 명칭을 말해보거라.')
     print("")
     print("")
     answer=input("병사 : 얼른 대답해보거라! : ")
     if answer == '을사조약' or answer == '을사늑약' :
        print("정답이다!")
        print("")
        print('병사2 : 중명전은 대한제국의 중요한 현장이다.')
        print("")
        print('        특히, 1904년 경운궁(현 덕수궁) 대화재 이후 중명전으로 거처를 옮긴 고종황제의 편전으로 사용되기도 했다.')
        print("")
        print('        또한 을사늑약의 부당함을 국제사회에 알리고자 1907년 4월 20일 헤이그 특사로 이준 등을 파견한 곳도 바로 중명전이다.')
        print("")
        print('병사2 : 다음으로 넘어가도 좋다. 탈출에 필요한 키워드는 (의) 이다.')
        qz5()
     else:
        answer = input("병사 : 틀렸다. 기회를 한번 더 주겠다 :")
        if answer == '을사조약' or answer == '을사늑약' :
            print("병사2 : 정답이다!")
            print('병사2 : 중명전은 대한제국의 중요한 현장니다.')
            print("")
            print('        특히, 1904년 경운궁(현 덕수궁) 대화재 이후 중명전으로 거처를 옮긴 고종황제의 편전으로 사용되기도 했다.')
            print("")
            print('        또한 을사늑약의 부당함을 국제사회에 알리고자 1907년 4월 20일 헤이그 특사로 이준 등을 파견한 곳도 바로 중명전이다.')
            print("")
            print('병사2 : 다음으로 넘어가도 좋다. 탈출에 필요한 키워드는 (의) 이다.')
            qz5()
        else:
            print("병사 : 틀렸다. 을사조약(을사늑약)이다. 널 감옥에 가두겠다.")
            print("")
            print('병사2 : 중명전은 대한제국의 중요한 현장니다.')
            print("")
            print('        특히, 1904년 경운궁(현 덕수궁) 대화재 이후 중명전으로 거처를 옮긴 고종황제의 편전으로 사용되기도 했다.')
            print("")
            print('        또한 을사늑약의 부당함을 국제사회에 알리고자 1907년 4월 20일 헤이그 특사로 이준 등을 파견한 곳도 바로 중명전이다.')
            print("")
            print('        이정도도 모르다니 알아두거라! ')
            print("")
            print("『게임종료』")


def qz5() :
      print("")
      print(line)
      print("")
      print('마지막 문제를 풀고 대한문 앞까지 온 당신은 타임머신을 찾았다.')
      print("")
      print('고종: 잠깐! 자네가 받은 키워드들을 가지고 정말 마지막 시험을 하겠다! 맞춘다면 이것을 돌려주지.')
      print("")
      print('      자네가 지나온 건물들은 모두 역사적인 사건이 남겨져있지... 마지막 문제를 맞추고 0000를 거두길 바라네')
      print("")
      print('      기회는 단 한번 뿐이다!')
      print("")
      print('해설: 키워드들을 가지고 조합하여 0000을 입력하십시오. <띄어쓰기는 없습니다>')
      print("")
      print('첫번째 키워드')
      print("")
      print(key1)
      print("")
      print('두번째 키워드')
      print("")
      print(key2)
      print("")
      print('세번째 키워드')
      print("")
      print(key3)
      print("")
      print('네번째 키워드')
      print("")
      print(key4)
      print("")
      print(line)
      print("")
      answer = input('고종: 답해보거라!  :')
      if answer == '유종의미' :
           print("")
           print('고종: 잘했구먼 허허... 자네 시대로 돌아가서도 이곳에 관심을 가져주길 바라네.')
           print("")
           print(line)
           print('타임머신을 타고 현재로 돌아온 당신은 덕수궁에 대해서 관심을 갖기 시작했습니다.')
           print("")
           print("")
           print(' 『축하드립니다! 덕수궁 탈출에 성공하셨습니다 !!』')
      else:
           print("")
           print('고종: 안타깝게도 자네는 마무리가 좋지 못하는구만...[유종의미]가 아닌가. 이자를 감옥에 가두거라!')
           print("")
           print('탈출에 실패하였습니다.')
           print("")
           print("")
           print("『게임종료』")





print("당신은 타임머신을 개발한 개발자입니다.")
print("")
print("시간을 2021년 10월 1일로 설정하고 타임머신을 작동시켰으나 오류로 인해 1910년의 덕수궁으로 시간 여행을 하게 되었습니다.")
print("")
print("")
print("현재, 타임머신의 기계를 문지기들이 대한문에 두었고 당신은 덕수궁을 탈출해 광화문으로 가서 타임머신을 되찾아 현실로 돌아와야 합니다.")
print(line)
print("덕수궁 안에 총 4개의 장소를 통과해야 광화문으로 갈 수 있습니다.")
print("첫 번째 관문인 석조전을 통과하세요.")
print("")
print("")
print("")
print("석조전을 탈출하기 위해선 문지기1 이 내는 문제를 맞춰야 합니다.")
print("")
print("")
print("")
print("문지기1 : 여기는 석조전이다. 지금부터 문제를 잘 듣고 다음에 대해 O 또는 X를 대답해보거라.")
print("")
print("문지기1 : 석조전은 해방 이후 미소공동위원회의 회담 장소로 쓰였을까?")
print("")
qz1()



          

    
