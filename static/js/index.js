function handleFileChange(e) {
    console.log(e.target.files[0])
}

function handleUpload(e) {
    
    console.log("handler triggered!")
}

//document.querySelector('.file-select').addEventListener('change', handleFileChange);
//document.querySelector('.file-submit').addEventListener('click', handleUpload);
var formdata = new FormData()
$('.file-select').change(function(e) {
    console.log('file changed!')
    console.log(e.target.files[0])
    formdata.append('imagefile', $('.file-select')[0].files[0])
})

url = "http://localhost:5000/convert"
$('.file-submit').click(function() { 
    console.log("clicked")
    $.ajax({
        url: url,
        type: "POST",
        data: formdata,
        success: function(data) {
            console.log('resp success')
        },
        error: function(error) {
            console.log("Error: ", error)
        } 

    })
  
})