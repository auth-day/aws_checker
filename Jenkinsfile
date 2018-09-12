node {
    def app

    stage('Clone repository') {

      checkout scm
    }
        
//    stage('Test') {
//        sh 'bash run_test.sh'
//        sh 'if [[ $? == "1" ]]; then echo "tests are faild" ; else exit 0 ; fi'
//    }
        
//    stage('Build image') {
//        CommitHash = sh(returnStdout: true, script: "git log -n 1 | head -n 1 | sed 's/commit//g'").trim()
//        BuildDate = sh(returnStdout: true, script: "git log -n 1 | tail -n 3 | head -n1 | sed 's/Date://g'").trim()
//        CommitOwner = sh(returnStdout: true, script: "git log -n 1 | head -n 2 | tail -n 1 | sed 's/Author://g'").trim()
//        app = docker.build("aws-checker", "--build-arg build_date='${BuildDate}' --build-arg commit_hash=${CommitHash} --build-arg commit_owner='${CommitOwner}' .")
//    }
    
//    stage('Push image') {
//        def stand = "dev"
//        docker.withRegistry('http://test2:5000') {
//            app.push("${stand}")
//       }
//    }
    
    stage('Push to Pypi') {
        sh 'python setup.py sdist upload -r pypi'
    }
 
}
