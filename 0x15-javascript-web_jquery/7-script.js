const api = "https://swapi-api.alx-tools.com/api/people/5/?format=json";

$.ajax({
    url: api,
    method: 'GET',
    dataType: 'json',
    success: function (data)
    {
        const name = data.name;
        $('div#character').text(name);
    },
    error: function (error)
    {
        console.log(error);
    }
});
