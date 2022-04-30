// inputタグで選択したファイルをimgタグに渡して表示させる
document.getElementById('input').addEventListener('change', e => {
  const file =e.target.files[0]; //filesに配列として画像を保存するのでインデックスが0番目のやつを取り出す
    if (!file) return;

    const reader = new FileReader();

    reader.onload = e => {
      document.getElementById('image').src = e.target.result
    };
    reader.readAsDataURL(file);
});

var cropper;

// トリミングボタンがクリックされたらcropperjsを作動
function inputChange(){
    var image = document.getElementById('image');
    cropper = new Cropper(image, {
      aspectRatio: 16 / 9,
      crop: function(e) {
        console.log(e.detail.x);
        console.log(e.detail.y);
        console.log(e.detail.width);
        console.log(e.detail.height);
        console.log(e.detail.rotate);
        console.log(e.detail.scaleX);
        console.log(e.detail.scaleY);
      }
    });
};

// トリミングしたのを生成してバックにpostする処理
function crop() {

  cropper.getCroppedCanvas().toBlob(function (blob) {
    const formData = new FormData();

    formData.append('croppedImage', blob);

    // Use `jQuery.ajax` method
    $.ajax('#', {
      method: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function () {
        console.log('Upload success');
      },
      error: function () {
        console.log('Upload error');
      }
    });
  });
};