# Markdown Practice

## Part1
_test itea_

**Bold Fond**

_**Iteal & Bold Font_**

Writing in Markdown is _not_ that hard!

**I will complete these lessons!**

_"Of course,"_ she whispered. Then, she shouted: "All I need is **a little moxie!**"

If you're thinking to yourself, **_This is unbelievable_**, you'd probably be right.

## Part2
# Header one
## Header two
### Header three
#### Header four
##### Header five
###### Header six

#### _Colombian Symbolism in One Hundred Years of Solitude_
Here's some words about the book _One Hundred Years..._.

[Search for it.](https://www.google.com/)

[You're _really, really_ going to want to see this.](https://www.dailykitten.com)

The Latest News from [the BBC](https://www.bbc.com/news)

## Part3

That's all there is to writing inline links.

另一種形式的連結稱為 參照連結。如同字面意思，這種連結實際上會參照文件中其他地方的內容。看不懂沒關係，考慮下方這個例子：

     Here's [a link to something else][another place].
     Here's [yet another link][another-link].
     And now back to [the first link][another place].

     [another place]: www.github.com
     [another-link]: www.google.com
  
例子中的「參照」是每行的第二組方括號：[another place] 及 [another-link]. 在 Markdown 文件的底部，這些方括號才被賦予確切網址的正式定義。這種參照連結的方式有個好處，就是多個指向相同地方的連結，可以使用標籤代稱，之後僅需統一對其賦予定義。比方說，我們決定將所有 [another place] 連結指向其他網站，不必一一修改，僅需改變參照本身的定義就好。

參照本身的定義內容，不會被彩現。它的格式為包著標籤的方括號，接著冒號，接著網址。

在下方的文字框，有一些寫到一半的參照連結，你的任務是將它們完成！將第一個參照標籤寫為「a fun place」，並讓它連結到 www.zombo.com；將第二個連結指向 www.stumbleupon.com。


Do you want to [see something fun][]?

Well, do I have [the website for you][another fun place]!

>>>>>>>>> https://www.markdowntutorial.com/zh-tw/lesson/3/
=======================
>>>>>>>>> https://www.markdowntutorial.com/zh-tw/lesson/3/
https://www.markdowntutorial.com/zh-tw/lesson/4/

如果你知道如何在 Markdown 中建立連結，那你也會插入圖片，因為兩者的語法十分相似。

同連結一樣，插入圖片也有兩種類型的寫法，且最終呈現的成果亦相同。圖片及連結在語法上的差別，在於插入圖片時，須以驚嘆號 ( ! ) 開頭。

第一種方式稱為 行內圖片連結，要建立行內的圖片連結，首先要打驚嘆號 ( ! )，將替代文字（為視障者描述圖片的一段文字）輸入在方括號 ( [ ] ) 裡，最後再將圖片的連結包在一對括號 ( ( ) ) 中。

舉例而言，要插入一張位於 https://octodex.github.com/images/bannekat.png 的圖片，其替代文字為 Benjamin Bannekat，在 Markdown 中的寫法為：![Benjamin Bannekat](https://octodex.github.com/images/bannekat.png)

作為練習，請在下方的文字框內，將這段連結改以圖片呈現，並在方括號填入一段替代文字「A pretty tiger」。



====
儘管替代文字並非 必填，但有了它會讓文件更容易被閱讀，包含視障者、使用螢幕閱讀器的讀者、或網路連線狀況不佳的人們。

接著我們要介紹的插入圖片的方式，就如同參照連結一般。你會以驚嘆號開頭，並以一對方括號包住替代文字，接著兩對表示圖片標籤的方括號，寫法如下： ![The founding father][Father] 在 Markdown 文件的底部，才定義了每個標籤指向的位址，像是： [Father]: http://octodex.github.com/images/founding-father.jpg

在下方的文字框，有些寫到一半的圖片連結，你的任務是以參照連結的方式將它們完成，就像上一堂課做的那樣。 將首個參照標籤設為「Black」並讓它連結到 https://upload.wikimedia.org/wikipedia/commons/a/a3/81_INF_DIV_SSI.jpg；讓第二幅圖片連結到 http://icons.iconarchive.com/icons/google/noto-emoji-animals-nature/256/22221-cat-icon.png


[Black cat][]

[Orange cat][Orange]

===
>>>>>>> https://www.markdowntutorial.com/zh-tw/lesson/5/

有時你需要將讀者的目光聚焦至一段引文，或是自雜誌文章上擷取某一段話，此時 Markdown 提供的 引用區塊 功能就十分方便。引用區塊的作用，是特別凸顯一段句子或段落，以吸引讀者的注意。例如：

"The sin of doing nothing is the deadliest of all the seven sins. It has been said that for evil men to accomplish their purpose it is only necessary that good men should do nothing."

插入引用區塊的方式，是在行首加入一個「大於」符號 (>)。例如：

> "In a few moments he was barefoot, his stockings folded in his pockets and his
  canvas shoes dangling by their knotted laces over his shoulders and, picking a
  pointed salt-eaten stick out of the jetsam among the rocks, he clambered down
  the slope of the breakwater."
在下方的文字框，將這段書本的引言改為引用區塊


I read this interesting quote the other day:

"Her eyes had called him and his soul had leaped at the call. To live, to err, to fall, to triumph, to recreate life out of life!"


====
你也可以在引文的行首插入一個大於符號 (>)，這在引文有多個篇幅時特別有用。例如：

> His words seemed to have struck some deep chord in his own nature. Had he spoken
of himself, of himself as he was or wished to be? Stephen watched his face for some
moments in silence. A cold sadness was there. He had spoken of himself, of his own
loneliness which he feared.
>
> —Of whom are you speaking? Stephen asked at length.
>
> Cranly did not answer.
注意到空行的行首也需要有大於符號 (>)，這樣才能使整段引用文字被正確辨識為同一區塊。

在下方的文字框，在每行行首插入一個大於符號 (>)，將內容變成引用區塊。


Once upon a time and a very good time it was there was a moocow coming down along the road and this moocow that was coming down along the road met a nicens little boy named baby tuckoo...

His father told him that story: his father looked at him through a glass: he had a hairy face.

He was baby tuckoo. The moocow came down the road where Betty Byrne lived: she sold lemon platt.

====
引用區塊當中可以包含其他 Markdown 元素，例如斜體字、圖片、連結。

在下方的文字框，將整段文字變成引用區塊，再將文末的法文標記為斜體字（不包含驚嘆號）。


He left her quickly, fearing that her intimacy might turn to jibing and wishing to be out of the way before she offered her ware to another, a tourist from England or a student of Trinity. Grafton Street, along which he walked, prolonged that moment of discouraged poverty. In the roadway at the head of the street a slab was set to the memory of Wolfe Tone and he remembered having been present with his father at its laying. He remembered with bitterness that scene of tawdry tribute. There were four French delegates in a brake and one, a plump smiling young man, held, wedged on a stick, a card on which were printed the words: VIVE L'IRLANDE!

===

>>>>>https://www.markdowntutorial.com/zh-tw/lesson/6/
本篇教學將介紹如何在 Markdown 中建立清單。

在已知的世界裡，有兩種類型的清單：無序清單及有序清單。用白話的方式解釋，前者就是以項目符號標記的，而後者是以數字標記的清單。

要建立無序清單，你需要以星號 ( * ) 做為每個項目的開頭，而且每個項目必須佔一行。比方說，要以 Markdown 書寫採買的清單，看起來會是：

* 牛奶
* 雞蛋
* 鮭魚
* 奶油
這份 Markdown 清單會以符號標記項目的方式呈現：

牛奶
雞蛋
鮭魚
奶油
在下方的文字框，將那些以逗號分隔的文字，改以清單呈現。


Flour, Cheese, Tomatoes

=====
以上就是撰寫無序清單的方法，那麼接下來介紹有序清單。

有序清單的項目是以數字開頭，而非星號。我們來看看這份食譜：

打三顆蛋
倒一加侖的牛奶到碗裡
用力地將奶油抹在鮭魚上
將鮭魚放進這碗蛋液及牛奶的混和液體裡
用 Markdown 怎麼寫呢？你要這樣做：

1. 打三顆蛋
2. 倒一加侖的牛奶到碗裡
3. 用力地將奶油抹在鮭魚上
4. 將鮭魚放進這碗蛋液及牛奶的混和液體裡
很簡單對不對？十分直覺。

在下方的文字框，以有序清單將剩下的食譜完成。

===
和你想的一樣，清單的項目中也可以有粗體、斜體字，甚至是連結。在下方的文字框，將植物的學名變成斜體。


Azalea (Ericaceae Rhododendron)
Chrysanthemum (Anthemideae Chrysanthemum)
Dahlia (Coreopsideae Dahlia)

=====
有時你發現需要撰寫多層次的清單，也稱作 巢狀清單，這種清單允許一個項目底下還有子項目。別怕，他們的 Markdown 語法都是相同的，你只需要在星號前比上層項目多加 一個空格 來縮排。

例如，為了更鉅細靡遺地描述各個人物，我們在底下的清單中使用了這樣的技巧，讓主要的項目底下還包含子清單。

* Tintin
 * 記者
 * 有一頭蓬蓬的橘頭髮
 * 他朋友有世界上最厲害的狗狗
* Haddock
 * 船長
 * 有超酷的鬍子
 * 喜歡喝威士忌
   * 可能是蘇格蘭人？
這些清單將以這樣的階層呈現

Tintin
記者
有一頭蓬蓬的橘頭髮
他朋友有世界上最厲害的狗狗
Haddock
船長
有超酷的鬍子
喜歡喝威士忌
可能是蘇格蘭人？
在下方的文字框，將每位角色的特質以多層次清單表示。


Calculus, A professor, Has no hair, Often wears green
Castafiore, An opera singer, Has white hair, Is possibly mentally unwell

======

厲害吧！雖然你的確可以無限延伸階層，但最多保持在三層比較好，否則看起來會一團亂。

我們還要介紹一個清單的縮排技巧，在撰寫段落的時候很好用。假如撰寫一份清單時，想要對其內容插入一些額外的補充資訊（但不是另一階層的清單），看起來像這樣：

打三顆蛋

打蛋時別弄到周圍了。

如果你 真的 搞砸了，拿條抹布擦乾淨。

倒一加侖的牛奶到碗裡

基本上，遵循上述的要點就對了：別灑出來，但如果發生了，就清理乾淨吧。

用力地將奶油抹在鮭魚上

「用力地」是指嚴格的上下移動。 Julia Child 曾說過：

Up and down and all around, that's how butter on salmon goes.

將鮭魚放進這碗蛋液及牛奶的溶液裡

放鮭魚時，有些事項需要注意：

確保周圍無障礙物及孩童
兩手並用
隨時準備一條抹布在旁，將灑出來的液體擦乾淨
要撰寫這樣的文本，段落的內容需在項目底下，且該行的行首至少要空一格。上例的清單，在 Markdown 的寫法如下：

1. 打三顆蛋

 打蛋時別弄到周圍了。
 如果你 _真的_ 搞砸了，拿條抹布擦乾淨。

2. 倒一加侖的牛奶到碗裡

 基本上，遵循上述的要點就對了：別灑出來，但如果發生了，就清理乾淨吧。

3. 用力地將奶油抹在鮭魚上

   「用力地」是指嚴格的上下移動。 Julia Child 曾說過：
   > Up and down and all around, that's how butter on salmon goes.
4. 將鮭魚放進這碗蛋液及牛奶的溶液裡

   * 確保周圍無障礙物及孩童
   * 兩手並用
   * 隨時準備一條抹布在旁，將灑出來的液體擦乾淨
  
注意到前兩個項目，它們底下的段落都各以一個空格開頭。如果你覺得這樣看起來很怪，也可以再鍵入幾個空白字元，將其適當對齊；同後兩個項目一樣。 在這些段落中，你可以插入各種 Markdown 元素，比如引用區塊，甚至是另一份清單！

在下方的文字框，將各子項目改以段落呈現。


Cut the cheese

Make sure that the cheese is cut into little triangles.
Slice the tomatoes

Be careful when holding the knife.
For more help on tomato slicing, see Thomas Jefferson's seminal essay Tom Ate Those.

=====
>>>>>> https://www.markdowntutorial.com/zh-tw/lesson/7/

段落（Paragraphs）
Markdown 有數種標記段落的方法。

作為範例，我們來看看幾行詩。假設你希望寫一段這樣的文字：

Do I contradict myself?
Very well then I contradict myself,
(I am large, I contain multitudes.)

你可能會想，這沒什麼難的，照每行的順序輸入就好：

Do I contradict myself?
Very well then I contradict myself,
(I am large, I contain multitudes.)
遺憾的是，事情並非如此。對 Markdown 語法而言，會將其呈現為同一行：Do I contradict myself? Very well then I contradict myself, (I am large, I contain multitudes.).

如果你硬是在他們之間插入空行，結果反而會將其分段，會變成：

Do I contradict myself?

Very well then I contradict myself,

(I am large, I contain multitudes.)
這樣的結果其實就是 硬換行（Hard break），然而對我們的詩而言，想要的是 軟換行（Soft break）。軟換行的標記方式，是在每行 行末 多輸入兩個空格字元。

Do I contradict myself?··
Very well then I contradict myself,··
(I am large, I contain multitudes.)
此處的點 ( · ) 是用來表示空格。

那麼就來練習這個技巧吧。在下方的文字框，插入適當數量的空格，好讓詩詞能正確呈現：


We pictured the meek mild creatures where They dwelt in their strawy pen, Nor did it occur to one of us there To doubt they were kneeling then.


======
除了用來排版詩詞，還有一個常用到軟換行的場合，是對清單裡的段落進行排版。回憶上一堂課的內容，我們在清單裡以插入空行的方式，來將多個段落分段。

在下方的文字框，將硬換行替換為軟換行，以縮緊子段落：


Crack three eggs over a bowl.

Now, you're going to want to crack the eggs in such a way that you don't make a mess.

If you do make a mess, use a towel to clean it up!

Pour a gallon of milk into the bowl.

Basically, take the same guidance as above: don't be messy, but if you are, clean it up!

=====
恭喜！
你已經完成了全部的課程！

不論你相不相信，我們才剛開始探索能以 Markdown 完成的事物。事實上，Markdown 有許多「延伸」的實作版本，支援了表格、定義清單、註腳……等功能。 但因為他們並非標準，對於瞭解基本用法也沒有助益，所以我們在課程並未提及。

如果你對於其他 Markdown 實作很感興趣，儘管去探索其他 Markdown 的 Apps 或教學。我們列出了一些：

https://daringfireball.net/projects/markdown/

https://spec.commonmark.org/dingus/

https://johnmacfarlane.net/babelmark2/faq.html

https://www.markdownguide.org

https://dave.autonoma.ca/blog/2019/05/22/typesetting-markdown-part-1/

http://idratherbewriting.com/2013/06/04/exploring-markdown-in-collaborative-authoring-to-publishing-workflows/

https://en.wikipedia.org/wiki/Markdown#Example

https://docs.gitlab.com/ee/user/markdown.html

https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

