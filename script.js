var client_id = process.env.client_id
var client_secret = process.env.client_secret   

var authOptions = {
    url: 'https://accounts.spotify.com/api/token',
    headers: {
        'Authorization' : 'Basic ' + (new Buffer.from(client_id + ':' + client_secret).toString('base64'))
    },
    form: {
        grant_type: 'client_crediental'
    },
    json: true
};

request.post(authOptions, function(error, response, body){
    if (!error && response.statusCode === 200) {
        var token = body.access_token;
       // console.log(token);
    }
});


