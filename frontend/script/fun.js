  var identity
  var check = true
  var tokenSplit = window.location.hash.split('#access_token=')[1]
  
  if(tokenSplit == undefined){
    check = false
  }else{
    var token = tokenSplit.split('&expires_in=7200')[0]

    $('.login').html("successful login")
    if(parseJwt(token).permissions.length > 1){
      $('#sellerOnly').append('<a href="selling.html"> <button type="button" class="btn btn-primary">sell product</button></a>')
      var but3 = '<button type="button" id="delete" class="btn btn-primary btn-lg">delete product</button>'
      $('#divID').append(but3)
      $('#delete').on("click",()=>{
        var idDELETE = window.location.search.substring(1)
        var tokenSplit = window.location.hash.split('#access_token=')[1]
        var token = ''
        if(tokenSplit == undefined){
            check = false
        }else{
             token = tokenSplit.split('&expires_in=7200')[0]
             function parseJwt () {
                var base64Url = token.split('.')[1];
                var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
                var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
                    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
                }).join(''));
                
                return JSON.parse(jsonPayload);
                };
        }
                  $.ajax({
                            url: 'https://udacityshopproject.herokuapp.com/delete/' + idDELETE,
                            type: 'delete',  
                            headers:{ 
                                       "Authorization": 'bearer ' + token
                                    }
                                      ,
                            
                            success: ()=>{
                              window.location.href = "index.html"
                            },
                            error: ()=>{
                              window.location.href = "index.html"
                            }
                            });
      })
    }
  }
function parseJwt () {
  var base64Url = token.split('.')[1];
  var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
  var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));
  
  return JSON.parse(jsonPayload);
};

$.ajax({
    dataType: "json",
    url: `https://udacityshopproject.herokuapp.com/home`,
    
    success: (result) => {
        var sellers = result
        seller = sellers['sellers'][0]
        for(var seller of sellers['sellers']){
          var id = seller.id
          var sellerID = id
          var link = 'seller.html'+ '?' + id
          var card_h5 = '<h5 class="card-title">'+ seller.product + '</h5>' 
          var card_p = '<p class="card-text">' + seller.description + '</p>'
          var card_a = '<a href="' + link + '" class="btn btn-primary" id="'+ seller.id +'">Go to seller</a>'
          var src = seller.image
          var img = '<img class="card-img-top" src="'+ src +'" alt="Card image cap">' 
  
  
          $('#cards').append('<div id="cards'+ seller.id +'1" class="card m-5" style="width: 18rem;"></div>')
  
          $('#cards'+ seller.id +'1').append(img)
          $('#cards'+ seller.id +'1').append('<div id="cards'+ seller.id +'2" class="card-body"></div>')
          $('#cards'+ seller.id +'2').append(card_h5)
          $('#cards'+ seller.id +'2').append(card_p)
          $('#cards'+ seller.id +'2').append(card_a)
          $('#'+ seller.id).on("click", (event)=>{
            
          })
        }
             
    
    },
    error: (error) => {
      
    }
  })


