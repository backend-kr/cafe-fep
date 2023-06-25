pipeline {
    agent any

    stages {
        stage('Check version') {
            steps {
                script {
                    // Shell 변수를 Groovy 변수로 변환
                    def REGISTRY="172.30.1.68:5000"
                    def IMAGE_NAME="cafe_fep-django"

                    // Shell 커맨드를 Groovy로 변환
                    def highestVersionOutput = sh(script: 'curl -s "http://' + REGISTRY + '/v2/' + IMAGE_NAME + '/tags/list" | jq -r ".tags[]" | grep -E "^[0-9]+\\\\.[0-9]+\\\\.[0-9]+(-dev-[0-9]+)?$" | sort -V | tail -1', returnStdout: true).trim()
                    def highestVersion = highestVersionOutput ? highestVersionOutput : "0.0.0"

                    def versionParts = highestVersion.split('-')
                    def baseVersion = versionParts[0]
                    def devVersion = versionParts[2] as Integer

                    def baseVersionParts = baseVersion.split('\\.')
                    def major = baseVersionParts[0]
                    def minor = baseVersionParts[1]
                    def build = baseVersionParts[2]

                    // dev_version 값 증가
                    devVersion += 1
                    def newVersion = "${major}.${minor}.${build}-dev-${devVersion}"
                }
            }
        }

        stage('Build image') {
            steps {
                script {
                    // 이미지 빌드
                    def DOCKER_CLI="docker"
                    sh "${DOCKER_CLI} build -t ${REGISTRY}/${IMAGE_NAME}:${newVersion} ."
                }
            }
        }

        stage('Push image') {
            steps {
                script {
                    // 이미지 푸시
                    sh "${DOCKER_CLI} push ${REGISTRY}/${IMAGE_NAME}:${newVersion}"

                    // 이전 이미지 정리
                    sh "echo 'y' | ${DOCKER_CLI} image prune -a"

                    // 최신 태그 업데이트
                    sh "${DOCKER_CLI} tag ${REGISTRY}/${IMAGE_NAME}:${newVersion} ${REGISTRY}/${IMAGE_NAME}:latest"
                    sh "${DOCKER_CLI} push ${REGISTRY}/${IMAGE_NAME}:latest"
                }
            }
        }
    }
}
