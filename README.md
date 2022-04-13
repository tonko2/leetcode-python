# leetcode_python

0001: 最初空のdictを用意してどんどん詰めてくともっとスッキリする.
0002: 解けなかった. 問題を読み間違えてた.
0020: 解けなかった. stackを使うとうまくいく.
0021: 解けなかった. ListNodeの仕様を理解できてない.
0053: 解けなかった. しゃくとりと累積和が思いついたが, オーダー的に累積和はダメ. しゃくとりはO(n)でできない.
0094: 
解けたけど時間かかった. inorder traversalは左に進んで, 進めなくなったら表示して右に進むを繰り返す. 
Inorder   -> (Left, Root, Right)
Preorder  -> (Root, Left, Right)
Postorder -> (Left, Right, Root)
0101: 解けなかった. t1.leftとt2.right, t1.rightとt2.leftを比較.