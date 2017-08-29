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
    </style>
  </head>

  <body>
    <div class="wrapper">
      <h1>Data Nasabah MongoBank!</h1>
      <div ><a href="tambah">Tambah Nasabah</a></div>
      <div class="guestbook">
        <h3>Data Nasabah:</h3>
        <table class="name" border="1" style="margin-bottom:50px;">
          <tr>
            <th>Nama</th>
            <th>Instansi</th>
            <th>Tabungan</th>
            <th>Aset (Jumlah)</th>
            <th>Nilai Aset</th>
            <th>Detail</th>
            <th>Opsi</th>
          </tr>
        %for data in nasabah:
          <tr>
            <td>{{data['nama']}}</td>
            <td>{{data['instansi']}}</td>
            <td>Rp. {{data['tabungan']}}</td>
            <td>{{data['aset']['nama']}} ({{data['aset']['jumlah']}})</td>
            <td>Rp. {{data['aset']['nilai']}}</td>
            <td><a href="/detail/{{data['_id']}}">Raw</a></td>
            <td><a href="/edit/{{data['_id']}}">Edit</a> | 
                <a href="/hapus/{{data['_id']}}">Hapus</a>
            </td>
          </tr>
        %end
        </table>
      </div>
      Diproses dalam: {{durasi}} detik
    </div>
  </body>
</html>