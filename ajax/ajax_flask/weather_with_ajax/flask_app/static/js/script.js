function get_current_weather(){
    // e.preventDefault();
    fetch("http://localhost:5000/api/weather/get")
    .then(resp => resp.json())
    .then(data => {
        // console.log(data);
        document.getElementById("location_name").innerText=data['name'];
        let dt=data['dt']+data['timezone'];
        let date=new Date(dt*1000);
        let format_date=date.toLocaleDateString('en-US', {weekday:"short", year:"numeric", month:"short", day:"numeric"});
        document.getElementById("current_date").innerText=format_date;
        document.getElementById("temp").innerText=Math.floor(data['main']['temp']);
        document.getElementById("temp_max").innerText=Math.floor(data['main']['temp_max']);
        document.getElementById("temp_min").innerText=Math.floor(data['main']['temp_min']);
        let iconCode=data['weather']['0']['icon'];
        let iconSRC=`http://openweathermap.org/img/wn/${iconCode}@2x.png`;
        let wxImg=document.getElementById("wx-img");
        wxImg.src=iconSRC;
        wxImg.alt=data['weather']['0']['description'];
        document.getElementById("description").innerText=data['weather']['0']['description'].replace(/\w\S*/g, (w) => (w.replace(/^\w/, (c) => c.toUpperCase())));
        document.getElementById("humidity").innerText=Math.floor(data['main']['humidity']);
        document.getElementById("wind").innerText=Math.floor(data['wind']['speed']);
    })
}

get_current_weather();