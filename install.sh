#!/bin/bash

# Check this packages
pkg=(python3 python3-pip)
pkg_manager=(apt brew)

# Check your default package manager and install packages
install_pkg () {
    if [[ $(which $1) && ! "not found" =~ $(which $1) ]]; then
        :
    else
        for manager in ${pkg_manager[*]}; do
            [[ $(which $manager) ]] && sudo $manager install $1 && return
        done
    fi
}

# Installing all packages that you dont have
install_all_pkg () {
    for x in ${pkg[*]}; do 
        install_pkg $x
    done
}

# Installing python3 requirements
install_python_req() {
    sudo pip3 install -r requirements.txt
}

# Main function
main () {
    install_all_pkg
    install_python_req
}

main