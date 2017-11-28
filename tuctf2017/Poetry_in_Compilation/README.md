Poetry in Compilation (200 points)
================================
```
Greetings, Hackerman - It is I, Hackerman

 Remember to finish up and submit your story to the erotic
 writing competition! In case your forget, you just need to
 use the PoemUpload tool and send it to poetry.tuctf.com:6663.

 I've gone ahead and copied the competition instructions below:

 Calling all erotica authors! For the competition, remember
 the following rules:

 All writing must be in fetlang
 If the writing is called with the argument:
    "echo"  - Return the next argument
	    - i.e. ./program echo hello -> outputs hello
    "count" - Return the number of letters in the next argument
	    - i.e. ./program count meowmeow -> 8
    "cat"   - Print the contents of a file in the next arg
	    - i.e. ./program cat flag.txt should return the
		     contents of a file called flag.txt

 Have fun, asipring authors!
```

In this challenges was it necessary to write fetlang code which did take two arguments as input. The parameter of the arguments is described in the description. 
I had never seen or written any fetlang before this challenges. So, I knew that this was going to be dirty. 

I found out fast that it was very few examples of writing fetlang code, but the exmaples which were included in the fetlang GitHub repo was enough. The one I used as a reference was brainfuck to C transpiler written in fetlang[1].

[1] [https://github.com/Property404/fetlang/blob/master/examples/bf2c.fet](https://github.com/Property404/fetlang/blob/master/examples/bf2c.fet)

Below is the code which was used to get the flag. This code were sent to an external server for validation, and since this service is down and I forgot to capture the flag will the flag not be shown here. 

```fetlang
make Amy moan "echo"
Make Betty moan "count"
Make Lise moan "cat"

Make Earl moan
Make Faith moan
Make Luna moan
Make Fucky moan

Worship Count feet

Worship Carrie's feet
Worship Zoro's cock
Lick Olivia's hair
Lick Per's left nipple two times
Lick Weird's left nipple three times

Bind Thomas to Saint Andrew's Cross
        have him hogtie Charlie
        Lick count
        If Thomas is Zoro's bitch
            If Carrie is Zoro's bitch
                make Earl moan Charlie's name
            If Carrie is Per's bitch
                make Luna moan Charlie's name
            If Carrie is Weird's bitch
                make Fucky moan Charlie's name
            lick Carrie's toes
            make Charlie moan
        if Charlie is Amy's bitch
                make Faith moan Charlie's name
                lick Carrie's toes
                make Charlie moan
                Have Count spank himself
        if Charlie is Betty's bitch
                make Faith moan Charlie's name
                lick Carrie's toes
                make Charlie moan
                Have Count spank himself
If Faith is Amy's fucktoy
    Make slave moan Fucky
    call safeword
If Faith is Betty's fuckboy
    Spank Count's butt two times
    make slave scream Count
    call safeword


(I have a fetish for obedience)
Lick Trisha's gums two times
(have Earl demand obedience of Luna)
if Carrie is submissive to Trisha
	make Dungeon Master moan "No input file\nUsage: "
	make Dungeon Master moan Earl's name
	make Dungeon Master scream " [file]"
	call safeword

have Luna demand obedience of Sonya
make slave moan Sonya's name
```

### Program in action

```
CTF :: CTF/tuctf/fetlang » ./a.out echo fetlang 
fetlang%  

CTF :: CTF/tuctf/fetlang » ./a.out count fetlang
seven

CTF :: CTF/tuctf/fetlang » ./a.out cat flag.txt 
flag{test_flag}
```

