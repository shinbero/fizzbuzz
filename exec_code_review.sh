set -u
set -o pipefail

function log() {
    echo -e "[$(date +"%Y-%m-%d %H:%M:%S%Z")]" "$@"
}

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color
function log_with_ok_or_ng() {
    local str=$1
    local ok_or_ng=$2

    if [[ $ok_or_ng == "ok" ]]; then
        log "${str} - [${GREEN}OK${NC}]"
    else
        log "${str} - [${RED}NG${NC}]"
    fi
}

function execute_check() {
    local check_type=$1
    local cmd=$2

    local num_unqualified=$(eval ${cmd} | wc -l)

    if [[ $num_unqualified == "0" ]]; then
        log_with_ok_or_ng "${check_type}" ok
    else
        log_with_ok_or_ng "${check_type}" ng

        # Show unquorified results.
        eval ${cmd}
        echo
    fi
}


execute_check "Cyclomatic Complexity check" "radon cc -s -n B **/*.py"
execute_check "Maintainability Index check" "radon mi -s -n B **/*.py"
execute_check "Coding style check" "flake8 **/*.py"

