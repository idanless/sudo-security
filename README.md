<p style="text-align: center;"><span style="text-decoration: underline;"><strong>About:</strong></span></p>
<p style="text-align: center;"><span style="font-weight: 400;">In this period we see many&nbsp; virus/malware&nbsp; target&nbsp; Linux&nbsp;</span></p>
<p style="text-align: center;"><span style="font-weight: 400;">the weak spot is not the escalation is the &lsquo;Users&rsquo; that have &ldquo;sudo&rdquo; and root and most time not aware the damage they can do on the to serves with this&nbsp; permission</span></p>
<p style="text-align: center;"><span style="font-weight: 400;">so i write this project help to IT and Security protect on Linux System</span></p>
<p style="text-align: center;"><span style="font-weight: 400;">if they not have dedicated software the company buy to do this</span></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>how this help ?</strong></p>
<p><span style="font-weight: 400;">because this python is give many ways to integration for example you can</span></p>
<p><span style="font-weight: 400;">assign it to the LDAP group&nbsp; for a list of commands or build profiles for users you don't trust in an easy way instead of changing the system configuration log user and any creative idea may have </span></p>
<p>&nbsp;</p>
<p style="text-align: center;"><span style="font-weight: 400;">we have 2 ways to implement (the easy ways)</span></p>
<p>&nbsp;</p>
<ol>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">copy sudo.py to &ldquo;/usr/local/bin/&rdquo;&nbsp;</span></li>
</ol>
<ul>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">chmod +x sudo.py</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">then change the name from sudo,py to to sudo by &ldquo;mv&rdquo; command&nbsp;</span></li>
<li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;">&nbsp;then you need not allow change&nbsp; only by root only</span></li>
</ul>
<p><span style="font-weight: 400;">&nbsp;&nbsp;sudo chattr +i&nbsp; /usr/local/bin/sudo&nbsp;</span></p>
<p><span style="font-weight: 400;">now logout / login any user from now use your &ldquo;sudo py&rdquo;&nbsp;</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">&nbsp; &nbsp; 2.</span><span style="font-weight: 400;">bese on&nbsp; &ldquo;profile&rdquo; any user that login in the first time to the linux server create a unique profile by his user this mean you can login as root edit and add &ldquo;alias&rdquo;</span></p>
<p><span style="font-weight: 400;">For example my username is &ldquo;Demo&rdquo; so I need to do &ldquo;nano&nbsp; /home/demo/.bashrc&rdquo; and my file is under tmp so -&gt; add this line &ldquo;alias sudo='python /tmp/sudo.py'&rdquo;.</span></p>
<p><span style="font-weight: 400;">also here recommended change by root only&nbsp; </span></p>
<p>&nbsp;</p>
<p><strong>note:</strong></p>
<p><span style="font-weight: 400;"><span style="text-decoration: underline;">most the OS linux should support basic Python3</span> but if </span></p>
<p><span style="font-weight: 400;">you want be sure the OS will run it</span></p>
<p><span style="font-weight: 400;">we can "compile it&rdquo; to be executable the compile must be running on same environment as</span></p>
<p><span style="font-weight: 400;">you target the first &ldquo;install by pip </span><span style="font-weight: 400;">pyinstaller</span><span style="font-weight: 400;">&rdquo;&nbsp; then running &ldquo;</span><span style="font-weight: 400;">pyinstaller --onefile sudo.py&rdquo;.</span></p>
<p><span style="font-weight: 400;">Last thing consider the script is clear text if you do not </span><span style="font-weight: 400;">compile&nbsp; it, be aware of that .</span></p>
<p><span style="font-weight: 400;">if you want avoid it also you can write simple shell script by same name call to python &ldquo;pyc&rdquo; this is compile file cannot be read&nbsp; (need&nbsp; convertor the py to pyc use&nbsp; py_compile)</span></p>
<p>&nbsp;</p>
<p style="text-align: left;">Demo[in the demo video im not allow for example running &ldquo;su&rdquo; ]:</p>
<p><a href="https://asciinema.org/a/lm5xs8ugeR07HAM6ntgpJfrBb" target="_blank"><img src="https://asciinema.org/a/lm5xs8ugeR07HAM6ntgpJfrBb.svg" /></a></p>
