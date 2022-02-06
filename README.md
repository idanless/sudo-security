<p><strong>About:</strong></p>
<p>Nowadays, we see many viruses or malwares&nbsp;that target&nbsp;different Linux&nbsp;OS distributions.</p>
<p>The weak spot is not the escalation, is the &lsquo;Users&rsquo; that have &ldquo;sudo&rdquo; and root and most od the time are not aware about the damage they can do to servers with root permission.</p>
<p>Target users: IT managers and Security teams that want to protect Linux Systems in companies without dedicated security or protection software.</p>
<p><strong>how this help ?</strong></p>
<p>I chose python to give flexibility for implementing and integrating the solution in different ways, for example:</p>
<p>Assign it to the LDAP group for a list of commands or build profiles for users you don't trust in a easy way instead of changing the system configuration log user etc ... &nbsp;any other creative ideas you may have can apply to integrating this package.</p>
<p>&nbsp;</p>
<p>we have 2 ways to implement (the easy ways)</p>
<ol>
<li>copy sudo.py to &ldquo;/usr/local/bin/&rdquo;&nbsp;</li>
</ol>
<ul>
<li>chmod +x sudo.py</li>
<li>Change the name from sudo,py to to sudo by &ldquo;mv&rdquo; command&nbsp;</li>
<li>&nbsp;You need not allow change&nbsp;only by root only<br />&nbsp;sudo chattr +i&nbsp; /usr/local/bin/sudo&nbsp;</li>
</ul>
<p>now logout / login with any user and from now on use your &ldquo;sudo py&rdquo;&nbsp;</p>
<p>&nbsp;</p>
<ol start="2">
<li>Based on&nbsp;user &ldquo;profile&rdquo;. Any user that login for the first time to the linux server create a unique profile. This means you can login as root, edit and add &ldquo;alias&rdquo;</li>
</ol>
<p>For example my username is &ldquo;Demo&rdquo; so I need to do &ldquo;nano&nbsp; /home/demo/.bashrc&rdquo; and my file is under tmp so -&gt; add this line &ldquo;alias sudo='python /tmp/sudo.py'&rdquo;.</p>
<p>also here recommended change by root only&nbsp;</p>
<p>&nbsp;</p>
<p><strong>note:</strong></p>
<p>Most of the Linux OS should support basic Python3&nbsp;but if you want to be sure the OS will run it, the package can be "compiled&rdquo; to an executable. The compile must run on same environment as you target the first &ldquo;install by pip&nbsp;pyinstaller&rdquo;&nbsp;then running &ldquo;pyinstaller --onefile sudo.py&rdquo;.</p>
<p>Last thing to consider, the script is in clear text. if you do not&nbsp;compile it, be aware!</p>
<p>If you want avoid it also you can write simple shell script by same name, call to python &ldquo;pyc&rdquo; this is the compiled file and cannot be read (need&nbsp;convertor the py to pyc use&nbsp; py_compile)</p>
<p>&nbsp;</p>
<p>Demo [in the demo video I do not allow running &ldquo;su&rdquo; (just an example)]:</p>
<p>&nbsp;</p>

<p><a href="https://asciinema.org/a/lm5xs8ugeR07HAM6ntgpJfrBb" target="_blank"><img src="https://asciinema.org/a/lm5xs8ugeR07HAM6ntgpJfrBb.svg" /></a></p>
