const { src, series, parallel, dest, watch, task } = require("gulp");
const browserSync = require("browser-sync").create();
// const exec = require('gulp-exec');
const { exec, execFile, spawn } = require('child_process');

var paths={
    styles:{
        src: 'assets/scss/**/*.scss',
        dest: 'static/css/**/*.css'
    }, 
    scripts:{
        src: 'assets/js/**/*.coffee',
        dest: 'static/js/**/*.js'
    }
};
// activate environment
function activate(){
    var activate_env = src('./**/*.py')
    .pipe(exec('python ../../pyenv/bin/activate_this.py', options))
}

// run flask server
function flask(flask_cb){
    var options = {
        continueOnError: false,
        pipeStdout: false,
        customTemplatingThing: "test"
    };
    var proc = execFile('./run.py',{ cwd:'../' }, ( error, stdout, stderr ) => {                
        if(error){ 
            throw error; 
        } else{
            console.log(stdout);
            console.log(stderr);
        }
    }); flask_cb();
}

function spawn_server(cb){    
    const flask = spawn('./run.py', { cwd: '../', detached:true });
    flask.stdout.on('data', (data) => {
        console.log(`$(data)`);
    });
    flask.stderr.on('data', (data) =>{
        console.log(data);
    });
    flask.on('close', (code) =>{
        console.log(`child process exited with code ${code}`);
    }); cb();
}

// browser-sync task
function bsync(done) {
    browserSync.init({
        watch: true,
        proxy: "localhost:3000",
        port: "4000"
    }); done();
}

function watchFiles(cb){
    watch("views.py", browserSync.reload);
    watch("models.py", browserSync.reload);
    watch("__init__.py", browserSync.reload);
    watch("templates/*.html", browserSync.reload);
    watch("static/css/*.css", browserSync.reload);
    cb();
}


exports.watchFiles = watchFiles;
exports.bsync = series(flask, bsync)
exports.server = spawn_server;
exports.default = flask;