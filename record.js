let shouldStop = false;
var downloadLink = document.getElementById('download');
var el = document.querySelector('.rbutton');
var record_button = document.getElementById('bid');
var audioCtx = new (window.AudioContext || webkitAudioContext)();
/*
var handleSuccess = function(stream) {
	var context = new AudioContext();
	var input = context.createMediaStreamSource(stream)
	var processor = context.createScriptProcessor(1024,1,1);

	source.connect(processor);
	processor.connect(context.destination);

	processor.onaudioprocess = function(e){
	  // Do something with the data, i.e Convert this to WAV
	  console.log(e.inputBuffer);
	};
};
*/
var handleSuccess = function(stream){
	console.log("handle success");
	const options = {mimeType: 'video/webm;codecs=vp9'};
	const recordedChunks = [];
	const mediaRecorder = new MediaRecorder(stream, options);
	//const mediaRecorder = new MediaRecorder(stream);  
	el.addEventListener('click', function(e){
	   if (bid.textContent == "START NOW") 
	   {
	       bid.textContent = "STOP";
	       shouldStop = false;
	       console.log(shouldStop);
	   }
	   else 
	   {
	     bid.textContent = "START NOW";
	     shouldStop = true;
	     console.log(shouldStop);
	   }
	});
	/*
	mediaRecorder.addEventListener('dataavailable', function(e) {
		console.log("data available");
	  if (e.data.size > 0) {
	    recordedChunks.push(e.data);
	  }

	  if(shouldStop == true) {
	    mediaRecorder.stop();
	  }
	});
	*/
	mediaRecorder.ondataavailable = function(e){
		console.log("data available");
	  if (e.data.size > 0) {
	    recordedChunks.push(e.data);
	  }

	  if(shouldStop == true) {
	    mediaRecorder.stop();
	  }		
	}
	/*
    mediaRecorder.addEventListener('stop', function() {
		console.log("stop");
		downloadLink.href = URL.createObjectURL(new Blob(recordedChunks));
		downloadLink.download = 'acetest.wav';
    });
    */
    mediaRecorder.onstop = function(){
		console.log("stop");
		downloadLink.href = URL.createObjectURL(new Blob(recordedChunks));
		downloadLink.download = 'acetest.wav';
    }
    mediaRecorder.start();
    console.log("media recorder started");
    console.log(mediaRecorder.state);
    //console.log(mediaRecorder.ondataavailable);

}

navigator.mediaDevices.getUserMedia({ audio: true, video: false }).then(handleSuccess);