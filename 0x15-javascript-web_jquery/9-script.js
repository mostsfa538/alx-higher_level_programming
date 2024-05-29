$.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    method: 'GET',
    dataType: 'json',
    success: function (data)
    {
        const hello = data.hello;
        $('DIV#hello').text(hello);
    },
    error: function (error)
    {
        console.log(error);
    }
});
