cmd_/home/csl/Desktop/Driver_linux/Module.symvers := sed 's/\.ko$$/\.o/' /home/csl/Desktop/Driver_linux/modules.order | scripts/mod/modpost -m -a  -o /home/csl/Desktop/Driver_linux/Module.symvers -e -i Module.symvers   -T -
