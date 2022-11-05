if [ "$#" -ne 1 ]; then
    echo "update_assignment.sh assignment_name"
else
	rm -r release/$1/
	nbgrader assign $1 --IncludeHeaderFooter.header=header.ipynb
fi
