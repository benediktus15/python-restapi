<!DOCTYPE html>
<html>
  <head>
    <title>Data Nasabah MongoBank!</title>
    <style type="text/css">
      body {font-family:sans-serif;color:#4f494f;}
      form input {border-radius: 7.5px;}
      h5 {display: inline;}
      .label {text-align: right}
      .guestbook {padding-top: 10px;}
      .name {width:100%; padding:3px;}
      .wrapper {padding: 25px;}
      .inputbox {width:98%;}
      .inputsh {width:95%;}
      .inputst {width:90%;}
    </style>
  </head>

  <body>
    <div class="wrapper">
      <h1>Tambah Data Nasabah MongoBank!</h1>
      <div ><a href="/">Home</a></div><br/>
      <div class="guestbook_input" >
      <form method="post" class="form" action="/newnasabah" method='post'>
      <table>

      <tr><td><b>Identitas Nasabah:</b></td> <td colspan="3"> </td></tr>
      <tr>
        <td>Nama: </td> <td colspan="3"><input type="text" name="nama" class="inputbox" /></td>
      </tr>
      <tr>
        <td>Email: </td> <td colspan="3"><input type="text" name="email" class="inputbox" /></td>
      </tr>
      <tr>
        <td>Instansi:</td> <td colspan="3"><input type="text" name="instansi" class="inputbox"/></td>
      </tr>
      <tr>
        <td>Alamat:</td> <td colspan="3"><input type="text" name="alamat" class="inputbox"/></td>
      </tr>
      <tr>
        <td>Telepon:</td> <td><input type="text" name="telepon" class="inputsh"/></td>
        <td>Umur:</td> <td><input type="text" name="umur" class="inputsh"/></td>
      </tr>
      <tr>
        <td>Jenis Kelamin:</td> <td><select name="gender">
                        <option value="male">male</option>
                        <option value="female">female</option>
                      </select></td>
        <td>Status Nikah:</td> <td><select name="status">
                        <option value="belum menikah">belum menikah</option>
                        <option value="menikah">menikah</option>
                      </select></td>
      </tr>

      <tr><td colspan="4"> <br/></td></tr>
      <tr><td><b>Detail Aset:</b></td> <td colspan="3"> </td></tr>
      <tr>
        <td>Aset:</td> <td><input type="text" name="aset"/></td>
        <td> </td> <td> </td>
      </tr>
      <tr>
        <td>Jumlah Aset:</td> <td><input type="text" name="jumlahaset"/></td>
        <td>Nilai:</td> <td>Rp. <input type="text" name="nilaiaset"/></td>
      </tr>

      <tr><td colspan="4"> <br/></td></tr>
      <tr><td><b>Tabungan:</b></td> <td colspan="3"> </td></tr>
      <tr>
        <td colspan="1">Tabungan Awal:</td>  <td colspan="3">Rp. <input type="text" name="tabungan" class="inputst" /></td>
      </tr>

      <tr><td colspan="4"> <br/></td></tr>
      <tr>
        <td colspan="4"><input type="submit" value='Tambah Nasabah'/></td>
      </tr>
        </table>
      </form>
      </div>
    </div>
  </body>
</html>