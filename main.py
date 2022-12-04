'''
    Author : Neel Vora
    Email: nxv8988@mavs.uta.edu
'''
from Rabin_Krap import Rabin_Karp as RK
from Knuth_Morris import Knuth_Morris as KM
import timeit
import matplotlib.pyplot as plt

if __name__=='__main__':

    time1=[]
    time2=[]
    input=[]
    pattern=[]
    x=[]
    input.append("MARCH # All Stories New and Complete Publisher Editor IF is published bi-monthly by Quinn Publishing Company, Inc., Kingston, New York. Volume #, No. #. Copyright # by Quinn Publishing Company, Inc. Application for Entry' as Second Class matter at Post Office, Buffalo, New York, pending. Subscription # for # issues in U.S. and Possessions: Canada # for # issues; elsewhere #. Aiiow four weeks for change of address. All stories appearing in this magazine are fiction. Any similarity to actual pers")
    input.append("Printed ia U.S.A chat with the editor i science fiction magazine called IF. The title was selected after much thought because of its brevity and on the theory it is indicative of the field and will be easy to remember. The tentative title that just morning and couldn't remember it until we'd had a cup of coffee, it was summarily discarded. A great deal of thought and effort lias gone into the formation of this magazine. We have had the aid of several very talented and generous people, for which we are most grateful. Much is due them for their warmhearted assistance. And now that the bulk of the formative work is done, we will try to maintain IF as one of the finest books on the market.  t a great public demand for our magazine. In short, why will you buy IF? We cannot, in honesty, say we will publish at all times the best science fiction in the field. That would not be true. But we will have access to the best stories, and we will get our fair s")
    input.append("We would rather think at all times in the terms of Some of the greatest escapist literature ever written, Treasure Island for instance, could be put into either category or both. And if Edgar Rice Burroughs is juvenile, then so are we, because the late master has given us some memorable thrills. Frankly, we don't think you'll buy IF because you feel we print better yams than any other mag. You will buy it, we hope, because you like its personality. Every magazine, we feel, does have a definite personality of its own. This personality is usually a reflection of the editors, their way of thinking, their appreciation of tKe market, their interpretation of what you will like best in stories and artwork. We have tried to make IF different from any other science fiction magazine on the stands while still building it along the lines of what every science fiction mag must be. Aside from the letter columns and the editorial, which are departments of field-wide use, we have not copied any feature of any other magazine. We will not, for instance, review fanzines, because we feel that is being most ably done by other mags. Nor will we, as a general practice, review books because that appears to us to be overdone. a personality of our own and hope thereby to establish an affinity with a large number of readers who will remember IF when they buy a science fiction mag as one they like and wish to continue reading. At all times we will hew to the story-line and will exhort with our writers to do the same. As an example, when Howard Browne phoned to talk over the plot for his lead novel in this issue, he described what ivas without doubt a staggering premise, a really startling concept he mourned, S T suppose I'll have to bend it around to give them the good old conventional ending."" We told Howard," "Not for IF, chum. Remember the old creed we live by. A writer may cheat on his wife, but he is ever true to the story-line. He may haul his infant son around by one leg.")
    input.append("but he carries a good story-idea like a holy relic. If there is only one logical ending for Twelve Times ZerG, that's the ending we want.Therefore, we do not feel the majority of readers necessarily want a happy ending regardless of all else. Not when it is incompatable with the aura of realism created by the writer. A check-list of fiction masterpieces certainly bears this out. The furor created by a little piece called Sorry , Wrong Number would certainly not have been forthcoming had the bedridden lady been rescued in the last paragraph. Romeo and Juliet would have beep nothing more than the smooth effort of the world's greatest writer if Romeo had gotten there in time. Yet, in modern fiction, he gets there in time with such amazing regularity one feels he has memorized at least  a dozen time-tables. The result has been unnumbered carloads of mediocre fiction. Also -- though we don't wish to underscore the point too heavily -- what could more surely have smothered the greatness of Wuthering Heights than a happy ending?  that IF will be a magazine given over to tragedy. W e will only insist that our writers create scenes and climaxes that fix the story rather than cater to that old formula. And in so doing we have an entirely selfish motive. This: As the years go by, we want to look back with personal pride upon an everlengthening list of great stories. So the book you now hold in your hands is a new one titled IF. We hope you will like it -- not for just a day -- not for just a month. But for years to come. pwf  Police grilled him mercilessly # while eyes from a hundred worlds looked on  It was a love-triangle murder that made today's headlines but the answer lay hundreds of thousands of light years away! one of the basement rooms. He moved slowly and with a kind of painful dignity, as a man moves on his way to the firing squad. A rumpled shock of black hair pointed up the extreme pallor of a gaunt face, empty at the moment of all expression. Harsh light from an overhead fixture winked back from tiny beads of perspiration dotting the waxen skin of his forehead. The three men with him watched him out of faces as expressionless as his own. They were ordinary men who wore ordinary clothing in an ordinary way. yet in the way they moved and in the w r ay they stood you knew they were I hard men who were in a hard and largely unpleasant business. One of them motioned casually toward a straight-backed chair almost exactly in the center of the room. Sit there, Cordell  I he said.  A quiet voice, not especially deep, yet its seemed to bounce off the painted concrete walls. Wordless, the young man obeyed. Sitting, he seemed as stiff and uncompromising as before. The man who had spoken made a vague gesture and the overhead light  went out, replaced simultaneously by strong rays from a spotlight aimed full at the eyes of the seated figure. Involuntarily the young man's head turned aside to avoid came out of the wall of darkness and jerked it back again. # 'Just to remind you , # the quiet voice continued conversationally, I'm Detective Lieutenant Kirk, Homicide Bureau . # A pair of hands thrust 'a second chair toward the circle of light. Kirk swung it around and dropped onto the seat, resting his arms along the back, facing the man across a distance of hardly more than inches. In the pitiless glare of the spotlight CordelPs cheekbones  stood out sharply, and under his deepset eyes were dark smudges of exhaustion. His rigid posture, h")
    input.append("We asked Howard and he asked this boss, Mr. Davis, and Mr. Davis said,Sure. oldest science-fiction publication in the world. It has the largest circulation in its field and up to January # th (the day IF went on the science fiction magazine your money could buy. It has the best writers in the field. Its departments are exfanzine reviews and Sam Merwin reviewing the books. So if you have a spare quarter, get a copy of And now, about Howard Browne. He is a huge man, made up almost entirely of vast enthusiasms. We have known Howard intimately for about six years and we continue to regard him with awe. There is no middle ground with this man. When he likes something, it's terrific If Howard hung a picture in his office we doubt if it would be a casual chore. The hammer he used would be a terrific hammer. The tack he drove would outshade other tacks by five country miles. And the picture? Gad, what a masterpiece! Seriously, one has only fo view Browne's enthusiasm for living to know it for what it is -- a priceless gift. He has written unnumbered short stories and, under the name of John Evans, is the father of near future. We have watched him write several of his stories and he hurled himself into each with a zeal and a zest that sfunned us into a partial paralysis. So we give you Howard Browne, a hard fellow to classify ; an astounding mixture of Balzac, a ten-ton dynamo, and Peter Pan. But this above all -- a great guy.  seemed not so much indications of defiance as they did the result of some terrible and deepseated shock, Let's go over it again, Cordell, Kirk said. The young man swallowed audibly against the silence. One of his hands twitched, came up almost to his face as though to shield hiseyes, then dropped limply back. That light --  he mumbled.  -- stays on , # Kirk said briskly. # The quicker you tell us the answers, the quicker we all relax. Okay? Cordell shook his head numbly, not so much in negation as an effort to clear the fog from his tortured mind. T told you,he cried hoarsely. What rpofe do you want? Yesterday I told you the whole thing. His voice began to border on hysteria. What good's my trying to tell you if you won't listen? How's a guy supposed -- " "Then try telling it straight!Kirk snapped. you think you're fooling around with half-wits? Sure ; you told us. A crazy pack of goof-ball dreams about a blonde babe clubbing two grown people to death, then disappearing in a ball of blue light! You figure on copping a plea on insanity?" "It's the truth! Cordell shouted. As God hears me, it's true! Suddenly he buried his face in his hands and long tearing sobs shook his slender frame. O ne of the other men reached out as though to drag the young man's face back into the withering rays of the spotlight, but Kirk motioned him away. Without haste the Lieutenant fished a cigar from the breast pocket of his coat and began almost leisurely to strip away its cellophane wrapper. A kitchen match burst into flame under the flick of a thumb nail and a cloud of blue tobacco smoke writhed into the cone of hot light. Cordell, Kirk said mildly. Slowly the young man's shoulders stopped their shaking, and after a long moment his wan, tearstained face came back into the light. I -- I'm sorry, he mumbled. Kirk waved away the layer of smoke hanging between them. He said wearily, Let's try it once more. Step by step. Maybe this time... He let the sentence trail off, but the inference was clear. An expression of hopeless resignation settled over Cordell's features. Where do you want me to start?" "Take it from five o'clock the afternoon it happened.The tortured man wet his lips. Five o'clock was when my shift went off at the plant. The plant, in case you've forgotten, is the Ames Chemical Company, and I'm a foreman in the Dry Packaging department." "Save your sarcasm, Kirk said equably. Yeah. I changed clothes and punched out around five-fifteen. Juanita had called me about four and said to pick her up at Professor Gilmore's laboratory, At what time?" "No special time. Just when I could get out there. We were going to have dinner and take in a movie. iN'o particular picture; she said we'd pick one out of the paper at dinner " "Go on . # Well, it must've been about quarter to six when I got out to the University. I parked in front of the laboratory wing and went in at the main entrance. I walked down the corridor to the Professors office. His typist was knocking out some letters and there were a couple of students hanging around waiting for him to show up. How about a smoke, Lieutenant? Kirk nodded to one of the men behind him and a package of cigarettes was extended to the man under the light. A match was proffered and the young man ignited the white tube, his hands shaking badly. The Lieutenant crossed his legs the other way. Let's hear the rest of it, friend." "What for? Bitterness tinged Cordell's voice. You don't believe a word I'm saying." "Up to now I do " "Well. I said something or other to Alma -- she's the Profs secretary -- and went on through the door to the hall that leads to the private lab. When I got -- #  K irk held up a hand. Wait a minute. Your busting right in on the Professor like that doesn't sound right. Why not wait in the office for your wife?" "What for? Cordell squinted at him in surprise. He and I get... , got along fine. When Juanita first went to work for him he said to drop in at the lab any time, not to wait in the outer office like a freshman or something." "Go ahead." "Well... The young man hesitated. We're back to the part you don't believe, Officer. I can't hardly believe it myself ; but so help me, it's gospel. I saw it!" "I'm waiting. Cordell said doggedly: The lab door was open a crack. I heard a woman's voice in there, and . it wasn't my wife's. It was a voice like -- like cracked ice. You know: cold and kind of... well... brittle and -- and deadly. That's the only way I can describe it. Anyway, I sort of hesitat")
    input.append("Printed is U.S.A chat with the editor i science fiction magazine called IF. The title was selected after much thought because of its brevity and on the theory it is indicative of the field and will be easy to remember. The tentative title that just morning and couldn't remember it until we'd had a cup of coffee, it was summarily discarded. A great deal of thought and effort lias gone into the formation of this magazine. We have had the aid of several very talented and generous people, for which we are most grateful. Much is due them for their warmhearted assistance. And now that the bulk of the formative work is done, we will try to maintain IF as one of the finest books on the market.  t a great public demand for our magazine. In short, why will you buy IF? We cannot, in honesty, say we will publish at all times the best science fiction in the field. That would not be true. But we will have access to the best stories, and we will get our fair s We would rather think at all times in the terms of Some of the greatest escapist literature ever written, Treasure Island for instance, could be put into either category or both. And if Edgar Rice Burroughs is juvenile, then so are we, because the late master has given us some memorable thrills. Frankly, we don't think you'll buy IF because you feel we print better yams than any other mag. You will buy it, we hope, because you like its personality. Every magazine, we feel, does have a definite personality of its own. This personality is usually a reflection of the editors, their way of thinking, their appreciation of tKe market, their interpretation of what you will like best in stories and artwork. We have tried to make IF different from any other science fiction magazine on the stands while still building it along the lines of what every science fiction mag must be. Aside from the letter columns and the editorial, which are departments of field-wide use, we have not copied any feature of any other magazine. We will not, for instance, review fanzines, because we feel that is being most ably done by other mags. Nor will we, as a general practice, review books because that appears to us to be overdone. a personality of our own and hope thereby to establish an affinity with a large number of readers who will remember IF when they buy a science fiction mag as one they like and wish to continue reading. At all times we will hew to the story-line and will exhort with our writers to do the same. As an example, when Howard Browne phoned to talk over the plot for his lead novel in this issue, he described what ivas without doubt a staggering premise, a really startling concept he mourned, S T suppose I'll have to bend it around to give them the good old conventional ending."" We told Howard," "Not for IF, chum. Remember the old creed we live by. A writer may cheat on his wife, but he is ever true to the story-line. He may haul his infant son around by one leg. but he carries a good story-idea like a holy relic. If there is only one logical ending for Twelve Times ZerG, that's the ending we want.Therefore, we do not feel the majority of readers necessarily want a happy ending regardless of all else. Not when it is incompatable with the aura of realism created by the writer. A check-list of fiction masterpieces certainly bears this out. The furor created by a little piece called Sorry , Wrong Number would certainly not have been forthcoming had the bedridden lady been rescued in the last paragraph. Romeo and Juliet would have beep nothing more than the smooth effort of the world's greatest writer if Romeo had gotten there in time. Yet, in modern fiction, he gets there in time with such amazing regularity one feels he has memorized at least  a dozen time-tables. The result has been unnumbered carloads of mediocre fiction. Also -- though we don't wish to underscore the point too heavily -- what could more surely have smothered the greatness of Wuthering Heights than a happy ending?  that IF will be a magazine given over to tragedy. W e will only insist that our writers create scenes and climaxes that fix the story rather than cater to that old formula. And in so doing we have an entirely selfish motive. This: As the years go by, we want to look back with personal pride upon an everlengthening list of great stories. So the book you now hold in your hands is a new one titled IF. We hope you will like it -- not for just a day -- not for just a month. But for years to come. pwf  Police grilled him mercilessly # while eyes from a hundred worlds looked on  It was a love-triangle murder that made today's headlines but the answer lay hundreds of thousands of light years away! one of the basement rooms. He moved slowly and with a kind of painful dignity, as a man moves on his way to the firing squad. A rumpled shock of black hair pointed up the extreme pallor of a gaunt face, empty at the moment of all expression. Harsh light from an overhead fixture winked back from tiny beads of perspiration dotting the waxen skin of his forehead. The three men with him watched him out of faces as expressionless as his own. They were ordinary men who wore ordinary clothing in an ordinary way. yet in the way they moved and in the w r ay they stood you knew they were I hard men who were in a hard and largely unpleasant business. One of them motioned casually toward a straight-backed chair almost exactly in the center of the room. Sit there, Cordell  I he said.  A quiet voice, not especially deep, yet its seemed to bounce off the painted concrete walls. Wordless, the young man obeyed. Sitting, he seemed as stiff and uncompromising as before. The man who had spoken made a vague gesture and the overhead light  went out, replaced simultaneously by strong rays from a spotlight aimed full at the eyes of the seated figure. Involuntarily the young man's head turned aside to avoid came out of the wall of darkness and jerked it back again. # 'Just to remind you , # the quiet voice continued conversationally, I'm Detective Lieutenant Kirk, Homicide Bureau . # A pair of hands thrust 'a second chair toward the circle of light. Kirk swung it around and dropped onto the seat, resting his arms along the back, facing the man across a distance of hardly more than inches. In the pitiless glare of the spotlight CordelPs cheekbones  stood out sharply, and under his deepset eyes were dark smudges of exhaustion. His rigid posture, We asked Howard and he asked this boss, Mr. Davis, and Mr. Davis said,Sure. oldest science-fiction publication in the world. It has the largest circulation in its field and up to January # th (the day IF went on the science fiction magazine your money could buy. It has the best writers in the field. Its departments are exfanzine reviews and Sam Merwin reviewing the books. So if you have a spare quarter, get a copy of And now, about Howard Browne. He is a huge man, made up almost entirely of vast enthusiasms. We have known Howard intimately for about six years and we continue to regard him with awe. There is no middle ground with this man. When he likes something, it's terrific If Howard hung a picture in his office we doubt if it would be a casual chore. The hammer he used would be a terrific hammer. The tack he drove would outshade other tacks by five country miles. And the picture? Gad, what a masterpiece! Seriously, one has only fo view Browne's enthusiasm for living to know it for what it is -- a priceless gift. He has written unnumbered short stories and, under the name of John Evans, is the father of near future. We have watched him write several of his stories and he hurled himself into each with a zeal and a zest that sfunned us into a partial paralysis. So we give you Howard Browne, a hard fellow to classify ; an astounding mixture of Balzac, a ten-ton dynamo, and Peter Pan. But this above all -- a great guy.  seemed not so much indications of defiance as they did the result of some terrible and deepseated shock, Let's go over it again, Cordell, Kirk said. The young man swallowed audibly against the silence. One of his hands twitched, came up almost to his face as though to shield hiseyes, then dropped limply back. That light --  he mumbled.  -- stays on , # Kirk said briskly. # The quicker you tell us the answers, the quicker we all relax. Okay? Cordell shook his head numbly, not so much in negation as an effort to clear the fog from his tortured mind. T told you,he cried hoarsely. What rpofe do you want? Yesterday I told you the whole thing. His voice began to border on hysteria. What good's my trying to tell you if you won't listen? How's a guy supposed -- " "Then try telling it straight!Kirk snapped. you think you're fooling around with half-wits? Sure ; you told us. A crazy pack of goof-ball dreams about a blonde babe clubbing two grown people to death, then disappearing in a ball of blue light! You figure on copping a plea on insanity?" "It's the truth! Cordell shouted. As God hears me, it's true! Suddenly he buried his face in his hands and long tearing sobs shook his slender frame. O ne of the other men reached out as though to drag the young man's face back into the withering rays of the spotlight, but Kirk motioned him away. Without haste the Lieutenant fished a cigar from the breast pocket of his coat and began almost leisurely to strip away its cellophane wrapper. A kitchen match burst into flame under the flick of a thumb nail and a cloud of blue tobacco smoke writhed into the cone of hot light. Cordell, Kirk said mildly. Slowly the young man's shoulders stopped their shaking, and after a long moment his wan, tearstained face came back into the light. I -- I'm sorry, he mumbled. Kirk waved away the layer of smoke hanging between them. He said wearily, Let's try it once more. Step by step. Maybe this time... He let the sentence trail off, but the inference was clear. An expression of hopeless resignation settled over Cordell's features. Where do you want me to start?" "Take it from five o'clock the afternoon it happened.The tortured man wet his lips. Five o'clock was when my shift went off at the plant. The plant, in case you've forgotten, is the Ames Chemical Company, and I'm a foreman in the Dry Packaging department." "Save your sarcasm, Kirk said equably. Yeah. I changed clothes and punched out around five-fifteen. Juanita had called me about four and said to pick her up at Professor Gilmore's laboratory, At what time?" "No special time. Just when I could get out there. We were going to have dinner and take in a movie. iN'o particular picture; she said we'd pick one out of the paper at dinner " "Go on . # Well, it must've been about quarter to six when I got out to the University. I parked in front of the laboratory wing and went in at the main entrance. I walked down the corridor to the Professors office. His typist was knocking out some letters and there were a couple of students hanging around waiting for him to show up. How about a smoke, Lieutenant? Kirk nodded to one of the men behind him and a package of cigarettes was extended to the man under the light. A match was proffered and the young man ignited the white tube, his hands shaking badly. The Lieutenant crossed his legs the other way. Let's hear the rest of it, friend." "What for? Bitterness tinged Cordell's voice. You don't believe a word I'm saying." "Up to now I do " "Well. I said something or other to Alma -- she's the Profs secretary -- and went on through the door to the hall that leads to the private lab. When I got -- #  K irk held up a hand. Wait a minute. Your busting right in on the Professor like that doesn't sound right. Why not wait in the office for your wife?" "What for? Cordell squinted at him in surprise. He and I get... , got along fine. When Juanita first went to work for him he said to drop in at the lab any time, not to wait in the outer office like a freshman or something." "Go ahead." "Well... The young man hesitated. We're back to the part you don't believe, Officer. I can't hardly believe it myself ; but so help me, it's gospel. I saw it!" "I'm waiting. Cordell said doggedly: The lab door was open a crack. I heard a woman's voice in there, and . it wasn't my wife's. It was a voice like -- like cracked ice. You know: cold and kind of... well... brittle and -- and deadly. That's the only way I can describe it. Anyway, I sort of hesitat")
    for i in input: x.append(len(i))

    pattern.append("all")
    pattern.append(" and ")
    pattern.append("the")
    pattern.append("after")
    pattern.append("of")
    pattern.append("is")
    prime_number=101

    
    for i in range(len(input)):
        print("Output from Rabin-Krap algorithm",end="\n")
        timein=timeit.default_timer()
        RK.search(pattern[i],input[i],prime_number)
        timeout=timeit.default_timer()
        time1.append(timeout-timein)

        print("Output from Knuth-Morris algorithm",end="\n")
        timein=timeit.default_timer()
        KM.KMPSearch(pattern[i],input[i])
        timeout=timeit.default_timer()
        time2.append(timeout-timein)

    
    plt.plot(x,time1, color='blue', marker='o', markerfacecolor='red', markersize=9, label="Rabin-Krap")
    plt.ylabel('Running time')
    plt.xlabel('Length of string')   
    plt.title('Rabin-Krap') 
    plt.xticks(ticks=x,rotation=90)
    plt.show()
    
    plt.plot(x,time2, color='blue', marker='o', markerfacecolor='red', markersize=9, label="knuth-Morris")
    plt.ylabel('Running time')
    plt.xlabel('Length of string')   
    plt.title('Knuth-Morris') 
    plt.xticks(ticks=x,rotation=90)   
    plt.show()

    plt.plot(x,time1, color='blue', marker='o', markerfacecolor='red', markersize=9, label="Rabin-Krap")
    plt.plot(x,time2, color='black', marker='o', markerfacecolor='orange', markersize=9, label="Knuth-Morris")
    plt.ylabel('Running time')
    plt.xlabel('Length of string')   
    plt.title('Rabin-Krap VS Knuth-Morris') 
    plt.xticks(ticks=x,rotation=90)
    plt.legend()    
    plt.show()