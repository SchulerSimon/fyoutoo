(function() {
	let v = undefined;
	setInterval(function() {

		// Only if ready, movie_player div loaded and when watching a video
		if (document.readyState !== 'complete' || ! document.getElementById("movie_player") || window.location.pathname != "/watch") {
			return;
		}

		// Stop all videos on page
                Array.from(document.getElementsByTagName("video")).forEach(e => e.pause);

		// Place player (or update if video has changed)
                let v2 = new URLSearchParams(window.location.search).get('v');
		if (!document.getElementById("youfucktube-player") || v != v2) {
                        v = v2;
                        let iframe = document.createElement('iframe');
                        iframe.id = "youfucktube-player";
                        iframe.style = "border-left: 2px solid darkred; width: 100%; height: 100%;";
                        iframe.title="YouFuckTubePlayer";
                        iframe.frameborder="0";
                        iframe.allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
                        iframe.allowfullscreen = "1";
                        iframe.src = "https://www.youtube.com/embed/" + v;
			document.getElementById("movie_player").innerHTML = iframe.outerHTML;
                        console.log("youfucktube-player placed");
		}

	}, 500);
})()