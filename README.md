# leetcode_python

0001: 最初空のdictを用意してどんどん詰めてくともっとスッキリする.
0002: 解けなかった. 問題を読み間違えてた.
0003: 解けた. しゃくとり法.
0005: 解けなかった. iをループさせて, 左と右が同じだったら, left -= 1, right += 1. max関数で文字列のlenを比較するときはkey=lenをつける.
0011: 解けた. 左端と右端から中央に向かって、探索. 大きい方を残す.
0015: 解けた. O(N^2 * logN) A + B == -Cとなるようなものがあるかを探す.
0017: 解けた. 再帰.
0019: 解けなかった. slow = head, fast = headでうまいことやって, headを返す.
0020: 解けなかった. stackを使うとうまくいく.
0021: 解けなかった. ListNodeの仕様を理解できてない.
0022: 解けた. 括弧の数を記憶してbacktrackすると、効率良く、短く書ける.
0053: 解けなかった. しゃくとりと累積和が思いついたが, オーダー的に累積和はダメ. しゃくとりはO(n)でできない.
0094: 
解けたけど時間かかった. inorder traversalは左に進んで, 進めなくなったら表示して右に進むを繰り返す. 
Inorder   -> (Left, Root, Right)
Preorder  -> (Root, Left, Right)
Postorder -> (Left, Right, Root)
0101: 解けなかった. t1.leftとt2.right, t1.rightとt2.leftを比較.
0141: O(1)で解けなかった. NodeごとSetで詰めればO(N)の実装は楽. O(1)は1個進むポインターと2個進むポインターを作って, 衝突したらループ
0155: 解けなかった. Stackの実装.
0160: 解けなかった. SpaceのO(N)解法 -> SetにheadAのNode詰めて, headBの中に同じNodeがあったらそれを返す. SpaceのO(1)解法 -> headAとheadB同時にずらして、最後までいったらheadB, headAにして繰り返す.
0169: 解けなかった. 候補を配列の1番目, cnt=1として持ち, 候補と一致してるかどうかでcntを増減させる. cntが0だった時, 候補を変える.
0206: 解けなかった. tailまでいって, head.nextをtailじゃなくprevに変える.
0226: 解けなかった. leftとrightを入れ替えて再帰.
0234: 解けなかった. 半分進めてreversed_listのポインターを作り, 残りの半分をslowとreversed_listで比較する.
0283: 解けなかった. pointerふたつ持って, slow = 0, fast = 0でループさせ, nums[slow] == 0 and nums[fast] != 0のとき, swapして, slow += 1
0543: 解けなかった. 木の直径を求める.
