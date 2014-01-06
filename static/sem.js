function sem(n, alpha, sigma, S, callback) {
  var obj = {
    n: n,
    alpha: alpha,
    sigma: sigma,
    S: S
  };
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      callback(JSON.parse(this.responseText));
    }
  };
  xhr.open('POST', '../sem');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify(obj));
}


function cov(data, callback) {
  var obj = {
    data: data
  };
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      callback(JSON.parse(this.responseText));
    }
  };
  xhr.open('POST', '../cov');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify(obj));
}
