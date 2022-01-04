
const currentLocation=document.getElementById("current_city");
getData(currentLocation);


function closeCookie(){
    document.querySelector("#cookie").remove();
}

function unitChange(element){
    if(element.value == "celcius"){
        for(var i=1; i<=8; i++){
            var tempId = "#t"+i;
            var fahrenheit = document.querySelector(tempId).innerText;
            var celcius = Math.round((fahrenheit-32)*(5/9));
            document.querySelector(tempId).innerText = celcius;
        }
    }
    else if(element.value == "fahrenheit"){
        for(var i=1; i<=8; i++){
            var tempId = "#t"+i;
            var celcius = document.querySelector(tempId).innerText;
            var fahrenheit = Math.round((celcius*(9/5))+32);
            document.querySelector(tempId).innerText = fahrenheit;
        }
    }
}


function getData(element){
    const apiKey=''
    const location = element.innerText;
    element.innerText=document.getElementById("current_city").innerText;
    element.city=document.getElementById("current_city").city;
    document.getElementById("current_city").innerText=location;
    document.getElementById('current_city').city=location;
    
    const CUR_API_URL = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}&units=imperial`;
    const FUT_API_URL = `https://api.openweathermap.org/data/2.5/forecast?q=${location}&appid=${apiKey}&units=imperial`;
    
    fetch(CUR_API_URL)
    .then(resp => resp.json())
    .then(data => {
        // console.log(data);
        highTemp = data['main']['temp_max'];
        lowTemp = data['main']['temp_min'];
        document.getElementById("t1").innerText = Math.floor(highTemp);
        document.getElementById("t2").innerText = Math.floor(lowTemp);
        document.getElementById("wd1").innerText = data['weather']['0']['description'];
        let iconCode=data['weather']['0']['icon'];
        let iconSRC=`http://openweathermap.org/img/wn/${iconCode}@2x.png`;
        let wxImg = document.getElementById('wi1');
        wxImg.src=iconSRC;
    })
    fetch(FUT_API_URL)
    .then(resp => resp.json())
    .then(data => {
        // console.log(data);
        dt=data['list']['11']['dt'];
        date=new Date(dt*1000);
        dayName=date.toLocaleDateString('en-US', {weekday: "long"});
        document.getElementById("dayThree").innerText=dayName;
        dt=data['list']['19']['dt'];
        date=new Date(dt*1000);
        dayName=date.toLocaleDateString('en-US', {weekday: "long"});
        document.getElementById("dayFour").innerText=dayName;
        
        for(var start=3; start <=19; start+=8){
            let min = data['list'][start]['main']['temp'];
            let max = data['list'][start]['main']['temp'];
            // console.log(`start: ${start} | min: ${min} | max: ${max}`);
            for(var stepper=0; stepper<8; stepper++){
                let temperature=data['list'][start+stepper]['main']['temp'];
                if(temperature>max){
                    max = temperature;
                }
                if(temperature<min){
                    min = temperature;
                }
                // console.log(`stepper: ${stepper} | temp: ${temperature} | min: ${min} | max: ${max}`);
            }
            if(start==3){
                document.getElementById("t3").innerText = Math.floor(max);
                document.getElementById("t4").innerText = Math.floor(min);
                document.getElementById("wd2").innerText = data['list'][start+4]['weather']['0']['description'];
                let iconCode=data['list'][start+4]['weather']['0']['icon'];
                let iconSRC=`http://openweathermap.org/img/wn/${iconCode}@2x.png`;
                let wxImg = document.getElementById('wi2');
                wxImg.src=iconSRC;
            }
            else if(start==11){
                document.getElementById("t5").innerText = Math.floor(max);
                document.getElementById("t6").innerText = Math.floor(min);
                document.getElementById("wd3").innerText = data['list'][start+4]['weather']['0']['description'];
                let iconCode=data['list'][start+4]['weather']['0']['icon'];
                let iconSRC=`http://openweathermap.org/img/wn/${iconCode}@2x.png`;
                let wxImg = document.getElementById('wi3');
                wxImg.src=iconSRC;
            }
            else if(start==19){
                document.getElementById("t7").innerText = Math.floor(max);
                document.getElementById("t8").innerText = Math.floor(min);
                document.getElementById("wd4").innerText = data['list'][start+4]['weather']['0']['description'];
                let iconCode=data['list'][start+4]['weather']['0']['icon'];
                let iconSRC=`http://openweathermap.org/img/wn/${iconCode}@2x.png`;
                let wxImg = document.getElementById('wi4');
                wxImg.src=iconSRC;
            }
        }

    })
}