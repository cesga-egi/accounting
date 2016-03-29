<div class="dtree">
        <script type="text/javascript">
                d = new dTree('d');

<?php include_once 'acct_portal.cfg'; ?>
<?php include_once 'dtree_storage.js'; ?>
                d.config.useLines = false;
                d.config.closeSameLevel = true;
                d.config.useStatusText = true;
                d.config.inOrder = true;
                document.write(d);

<?php
function selfURL() { $s = empty($_SERVER["HTTPS"]) ? '' : ($_SERVER["HTTPS"] == "on") ? "s" : ""; $protocol = strleft(strtolower($_SERVER["SERVER_PROTOCOL"]), "/").$s; $port = ($_SERVER["SERVER_PORT"] == "80") ? "" : (":".$_SERVER["SERVER_PORT"]); return $protocol."://".$_SERVER['SERVER_NAME'].$port.$_SERVER['REQUEST_URI']; } function strleft($s1, $s2) { return substr($s1, 0, strpos($s1, $s2)); }

	$type = htmlspecialchars($_GET[type]);
	print " d.openTo(egiid,true);\n";
?>
        </script>
</div>

<p>&nbsp;</p>
<img src="http://chart.googleapis.com/chart?chs=120x120&cht=qr&choe=UTF-8&chl=<?=urlencode(selfURL());?>" alt="QR Code"/>
<table class='devby'>
 <tr>
  <td nowrap>
Developed by <a href="http://www.cesga.es/index.php?lang=en" target="_blank"><img src="core/images/cesga_pq1.jpg" alt="http://www.cesga.es/index.php?lang=en" border=0></a>
  </td>
 </tr>
</table>
