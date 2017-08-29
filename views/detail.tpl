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
      <h1>Edit Data Nasabah MongoBank!</h1>
      <div ><a href="/">Home</a></div><br/>
      <b>Raw Data:</b><br/>
      {{nasabah}}

      <br/>
      <br/>

      %for data in nasabah:
      <div class="guestbook_input" >
      <table>

      <tr><td><b>Identitas Nasabah:</b></td> <td colspan="3">id: {{data['_id']}}</td></tr>
      <tr>
      <tr>
        <td>Nama: </td> <td colspan="3"><input type="text" name="nama" value="{{data['nama']}}" class="inputbox" disabled /></td>
      </tr>
      <tr>
        <td>Email: </td> <td colspan="3"><input type="text" name="email" value="{{data['email']}}" class="inputbox" disabled /></td>
      </tr>
      <tr>
        <td>Instansi:</td> <td colspan="3"><input type="text" name="instansi" value="{{data['instansi']}}" class="inputbox" disabled /></td>
      </tr>
      <tr>
        <td>Alamat:</td> <td colspan="3"><input type="text" name="alamat" value="{{data['alamat']}}" class="inputbox" disabled /></td>
      </tr>
      <tr>
        <td>Telepon:</td> <td><input type="text" name="telepon" value="{{data['telepon']}}" disabled /></td>
        <td>Umur:</td> <td><input type="text" name="umur" value="{{data['umur']}}" disabled /></td>
      </tr>
      <tr>
        <td>Jenis Kelamin:</td> <td><select name="gender" disabled>
                        <option value="{{data['gender']}}">{{data['gender']}}</option>
                        <option value="male">male</option>
                        <option value="female">female</option>
                      </select></td>
        <td>Status Nikah:</td> <td><select name="status" disabled>
                        <option value="{{data['status']}}">{{data['status']}}</option>
                        <option value="belum nikah">belum nikah</option>
                        <option value="nikah">nikah</option>
                      </select></td>
      </tr>

      <tr><td colspan="4"> <br/></td></tr>
      <tr><td><b>Detail Aset:</b></td> <td colspan="3"> </td></tr>
       <tr>
        <td>Aset:</td> <td><input type="text" name="aset" value="{{data['aset']['nama']}}" disabled /></td>
        <td> </td> <td> </td>
      </tr>
      <tr>
        <td>Jumlah Aset:</td> <td><input type="text" name="jumlahaset" value="{{data['aset']['jumlah']}}" disabled /></td>
        <td>Nilai:</td> <td>Rp. <input type="text" name="nilaiaset" value="{{data['aset']['nilai']}}" disabled /></td>
      </tr>

      <tr><td colspan="4"> <br/></td></tr>
      <tr><td><b>Tabungan:</b></td> <td colspan="3"> </td></tr>
      <tr>
        <td colspan="1">Tabungan Awal:</td>  <td colspan="3">Rp. <input type="text" name="tabungan" value="{{data['tabungan']}}" style="width:80%" disabled /></td>
      </tr>
        </table>
      </div>
      %end
      <br/><br/>
      Diproses dalam: {{durasi}} detik
    </div>
  </body>
</html>