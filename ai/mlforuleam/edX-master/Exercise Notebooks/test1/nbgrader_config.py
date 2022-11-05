c = get_config()

###############################################################################
# Begin additions by nbgrader quickstart
###############################################################################

# You only need this if you are running nbgrader on a shared
# server set up.
c.NbGrader.course_id = "test1"

# Update this list with other assignments you want
c.NbGrader.db_assignments = [dict(name="ps1")]

# Change the students in this list with that actual students in
# your course
c.NbGrader.db_students = [
    dict(id="bitdiddle", first_name="Ben", last_name="Bitdiddle"),
    dict(id="hacker", first_name="Alyssa", last_name="Hacker"),
    dict(id="reasoner", first_name="Louis", last_name="Reasoner")
]

###############################################################################
# End additions by nbgrader quickstart
###############################################################################

# Configuration file for nbgrader.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

## This is an application.

## The date format used by logging formatters for %(asctime)s
#c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#c.Application.log_level = 30

#------------------------------------------------------------------------------
# JupyterApp(Application) configuration
#------------------------------------------------------------------------------

## Base class for Jupyter applications

## Answer yes to any prompts.
#c.JupyterApp.answer_yes = False

## Full path of a config file.
#c.JupyterApp.config_file = ''

## Specify a config file to load.
#c.JupyterApp.config_file_name = ''

## Generate default config file.
#c.JupyterApp.generate_config = False

#------------------------------------------------------------------------------
# NbGrader(JupyterApp) configuration
#------------------------------------------------------------------------------

## A base class for all the nbgrader apps.

## The assignment name. This MUST be specified, either by setting the config
#  option, passing an argument on the command line, or using the --assignment
#  option on the command line.
#c.NbGrader.assignment_id = ''

## The name of the directory that contains assignment submissions after they have
#  been autograded. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#c.NbGrader.autograded_directory = 'autograded'

## The root directory for the course files (that includes the `source`,
#  `release`, `submitted`, `autograded`, etc. directories). Defaults to the
#  current working directory.
#c.NbGrader.course_directory = ''

## A key that is unique per instructor and course. This MUST be specified, either
#  by setting the config option, or using the --course option on the command
#  line.
#c.NbGrader.course_id = ''

## A list of assignments that will be created in the database. Each item in the
#  list should be a dictionary with the following keys:
#  
#      - name
#      - duedate (optional)
#  
#  The values will be stored in the database. Please see the API documentation on
#  the `Assignment` database model for details on these fields.
#c.NbGrader.db_assignments = []

## A list of student that will be created in the database. Each item in the list
#  should be a dictionary with the following keys:
#  
#      - id
#      - first_name (optional)
#      - last_name (optional)
#      - email (optional)
#  
#  The values will be stored in the database. Please see the API documentation on
#  the `Student` database model for details on these fields.
#c.NbGrader.db_students = []

## URL to the database. Defaults to sqlite:///<course_directory>/gradebook.db,
#  where <course_directory> is another configurable variable.
#c.NbGrader.db_url = ''

## Format string for the directory structure that nbgrader works over during the
#  grading process. This MUST contain named keys for 'nbgrader_step',
#  'student_id', and 'assignment_id'. It SHOULD NOT contain a key for
#  'notebook_id', as this will be automatically joined with the rest of the path.
#c.NbGrader.directory_structure = '{nbgrader_step}/{student_id}/{assignment_id}'

## The name of the directory that contains assignment feedback after grading has
#  been completed. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#c.NbGrader.feedback_directory = 'feedback'

## List of file names or file globs to be ignored when copying directories.
#c.NbGrader.ignore = ['.ipynb_checkpoints', '*.pyc', '__pycache__']

## Name of the logfile to log to.
#c.NbGrader.logfile = '.nbgrader.log'

## File glob to match notebook names, excluding the '.ipynb' extension. This can
#  be changed to filter by notebook.
#c.NbGrader.notebook_id = '*'

## The name of the directory that contains the version of the assignment that
#  will be released to students. This corresponds to the `nbgrader_step` variable
#  in the `directory_structure` config option.
#c.NbGrader.release_directory = 'release'

## The name of the directory that contains the master/instructor version of
#  assignments. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#c.NbGrader.source_directory = 'source'

## File glob to match student IDs. This can be changed to filter by student.
#  Note: this is always changed to '.' when running `nbgrader assign`, as the
#  assign step doesn't have any student ID associated with it.
#c.NbGrader.student_id = '*'

## The name of the directory that contains assignments that have been submitted
#  by students for grading. This corresponds to the `nbgrader_step` variable in
#  the `directory_structure` config option.
#c.NbGrader.submitted_directory = 'submitted'

#------------------------------------------------------------------------------
# NbGraderApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# TransferApp(NbGrader) configuration
#------------------------------------------------------------------------------

## A base class for the list, release, collect, fetch, and submit apps.
#  
#  All of these apps involve transfering files between an instructor or students
#  files and the nbgrader exchange.

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#c.TransferApp.cache_directory = ''

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#c.TransferApp.exchange_directory = '/srv/nbgrader/exchange'

## Whether the path for fetching/submitting  assignments should be prefixed with
#  the course name. If this is `False`, then the path will be something like
#  `./ps1`. If this is `True`, then the path will be something like
#  `./course123/ps1`.
#c.TransferApp.path_includes_course = False

## Format string for timestamps
#c.TransferApp.timestamp_format = '%Y-%m-%d %H:%M:%S %Z'

## Timezone for recording timestamps
#c.TransferApp.timezone = 'UTC'

#------------------------------------------------------------------------------
# SubmitApp(TransferApp) configuration
#------------------------------------------------------------------------------

## Whether or not to submit the assignment if there are missing notebooks from
#  the released assignment notebooks.
#c.SubmitApp.strict = False

#------------------------------------------------------------------------------
# ListApp(TransferApp) configuration
#------------------------------------------------------------------------------

## Print out assignments as json
#c.ListApp.as_json = False

## List assignments in submission cache.
#c.ListApp.cached = False

## List inbound files rather than outbound.
#c.ListApp.inbound = False

## Remove, rather than list files.
#c.ListApp.remove = False

#------------------------------------------------------------------------------
# NbConvertApp(JupyterApp) configuration
#------------------------------------------------------------------------------

## This application is used to convert notebook files (*.ipynb) to various other
#  formats.
#  
#  WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.

## The export format to be used, either one of the built-in formats, or a dotted
#  object name that represents the import path for an `Exporter` class
#c.NbConvertApp.export_format = 'html'

## read a single notebook from stdin.
#c.NbConvertApp.from_stdin = False

## List of notebooks to convert. Wildcards are supported. Filenames passed
#  positionally will be added to the list.
#c.NbConvertApp.notebooks = []

## overwrite base name use for output files. can only be used when converting one
#  notebook at a time.
#c.NbConvertApp.output_base = ''

## Directory to copy extra files (figures) to. '{notebook_name}' in the string
#  will be converted to notebook basename
#c.NbConvertApp.output_files_dir = '{notebook_name}_files'

## PostProcessor class used to write the results of the conversion
#c.NbConvertApp.postprocessor_class = ''

## Whether to apply a suffix prior to the extension (only relevant when
#  converting to notebook format). The suffix is determined by the exporter, and
#  is usually '.nbconvert'.
#c.NbConvertApp.use_output_suffix = True

## Writer class used to write the  results of the conversion
#c.NbConvertApp.writer_class = 'FilesWriter'

#------------------------------------------------------------------------------
# ValidateApp(NbGrader,NbConvertApp) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# BaseNbConvertApp(NbGrader,NbConvertApp) configuration
#------------------------------------------------------------------------------

## This application is used to convert notebook files (*.ipynb) to various other
#  formats.
#  
#  WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.

## Whether to overwrite existing assignments/submissions
#c.BaseNbConvertApp.force = False

## Permissions to set on files output by nbgrader. The default is generally read-
#  only (444), with the exception of nbgrader assign, in which case the user also
#  has write permission.
#c.BaseNbConvertApp.permissions = 0

#------------------------------------------------------------------------------
# FeedbackApp(BaseNbConvertApp) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# AutogradeApp(BaseNbConvertApp) configuration
#------------------------------------------------------------------------------

## Whether to create the student at runtime if it does not already exist.
#c.AutogradeApp.create_student = False

#------------------------------------------------------------------------------
# ExtensionApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# ReleaseApp(TransferApp) configuration
#------------------------------------------------------------------------------

## Force overwrite existing files in the exchange.
#c.ReleaseApp.force = False

#------------------------------------------------------------------------------
# FormgradeApp(NbGrader) configuration
#------------------------------------------------------------------------------

## Authenticator used in all formgrade requests.
#c.FormgradeApp.authenticator_class = 'nbgrader.auth.noauth.NoAuth'

## IP address for the server
#c.FormgradeApp.ip = 'localhost'

## URL or local path to mathjax installation. Defaults to the version of MathJax
#  included with the Jupyter Notebook.
#c.FormgradeApp.mathjax_url = ''

## Port for the server
#c.FormgradeApp.port = 5000

#------------------------------------------------------------------------------
# UpdateApp(NbGrader) configuration
#------------------------------------------------------------------------------

## whether to validate metadata after updating it
#c.UpdateApp.validate = True

#------------------------------------------------------------------------------
# QuickStartApp(NbGrader) configuration
#------------------------------------------------------------------------------

## Whether to overwrite existing files
#c.QuickStartApp.force = False

#------------------------------------------------------------------------------
# AssignApp(BaseNbConvertApp) configuration
#------------------------------------------------------------------------------

## Whether to create the assignment at runtime if it does not already exist.
#c.AssignApp.create_assignment = False

## Do not save information about the assignment into the database.
#c.AssignApp.no_database = False

#------------------------------------------------------------------------------
# ExportApp(NbGrader) configuration
#------------------------------------------------------------------------------

## The plugin class for exporting the grades.
#c.ExportApp.plugin_class = 'nbgrader.plugins.export.CsvExportPlugin'

#------------------------------------------------------------------------------
# CollectApp(TransferApp) configuration
#------------------------------------------------------------------------------

## Update existing submissions with ones that have newer timestamps.
#c.CollectApp.update = False

#------------------------------------------------------------------------------
# FetchApp(TransferApp) configuration
#------------------------------------------------------------------------------

## Whether to replace missing files on fetch
#c.FetchApp.replace_missing_files = False

#------------------------------------------------------------------------------
# DbApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# LateSubmissionPlugin(BasePlugin) configuration
#------------------------------------------------------------------------------

## Predefined methods for assigning penalties for late submission

## The method for assigning late submission penalties:
#      'none': do nothing (no penalty assigned)
#      'zero': assign an overall score of zero (penalty = score)
#c.LateSubmissionPlugin.penalty_method = 'none'

#------------------------------------------------------------------------------
# ExportPlugin(BasePlugin) configuration
#------------------------------------------------------------------------------

## Base class for export plugins.

## destination to export to
#c.ExportPlugin.to = ''

#------------------------------------------------------------------------------
# CsvExportPlugin(ExportPlugin) configuration
#------------------------------------------------------------------------------

## CSV exporter plugin.

#------------------------------------------------------------------------------
# NbConvertBase(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## Global configurable class for shared config
#  
#  Useful for display data priority that might be used by many transformers

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#c.NbConvertBase.default_language = 'ipython'

## An ordered list of preferred output type, the first encountered will usually
#  be used when converting discarding the others.
#c.NbConvertBase.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#------------------------------------------------------------------------------
# Preprocessor(NbConvertBase) configuration
#------------------------------------------------------------------------------

## A configurable preprocessor
#  
#  Inherit from this class if you wish to have configurability for your
#  preprocessor.
#  
#  Any configurable traitlets this class exposed will be configurable in profiles
#  using c.SubClassName.attribute = value
#  
#  you can overwrite :meth:`preprocess_cell` to apply a transformation
#  independently on each cell or :meth:`preprocess` if you prefer your own logic.
#  See corresponding docstring for informations.
#  
#  Disabled by default and can be enabled via the config by
#      'c.YourPreprocessorName.enabled = True'

## 
#c.Preprocessor.enabled = False

#------------------------------------------------------------------------------
# NbGraderPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------

## Whether to use this preprocessor when running nbgrader
#c.NbGraderPreprocessor.enabled = True

#------------------------------------------------------------------------------
# AssignLatePenalties(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## Preprocessor for assigning penalties for late submissions to the database

## The plugin class for assigning the late penalty for each notebook.
#c.AssignLatePenalties.plugin_class = 'nbgrader.plugins.latesubmission.LateSubmissionPlugin'

#------------------------------------------------------------------------------
# IncludeHeaderFooter(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor for adding header and/or footer cells to a notebook.

## Path to footer notebook
#c.IncludeHeaderFooter.footer = ''

## Path to header notebook
#c.IncludeHeaderFooter.header = ''

#------------------------------------------------------------------------------
# LockCells(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor for making cells undeletable.

## Whether all assignment cells are locked (non-deletable and non-editable)
#c.LockCells.lock_all_cells = False

## Whether grade cells are locked (non-deletable)
#c.LockCells.lock_grade_cells = True

## Whether readonly cells are locked (non-deletable and non-editable)
#c.LockCells.lock_readonly_cells = True

## Whether solution cells are locked (non-deletable and non-editable)
#c.LockCells.lock_solution_cells = True

#------------------------------------------------------------------------------
# ClearSolutions(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## The delimiter marking the beginning of a solution
#c.ClearSolutions.begin_solution_delimeter = 'BEGIN SOLUTION'

## The code snippet that will replace code solutions
#c.ClearSolutions.code_stub = {'python': '# YOUR CODE HERE\nraise NotImplementedError()'}

## The delimiter marking the end of a solution
#c.ClearSolutions.end_solution_delimeter = 'END SOLUTION'

## Whether or not to complain if cells containing solutions regions are not
#  marked as solution cells. WARNING: this will potentially cause things to break
#  if you are using the full nbgrader pipeline. ONLY disable this option if you
#  are only ever planning to use nbgrader assign.
#c.ClearSolutions.enforce_metadata = True

## The text snippet that will replace written solutions
#c.ClearSolutions.text_stub = 'YOUR ANSWER HERE'

#------------------------------------------------------------------------------
# SaveAutoGrades(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## Preprocessor for saving out the autograder grades into a database

#------------------------------------------------------------------------------
# DisplayAutoGrades(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## Preprocessor for displaying the autograder grades

## Print out validation results as json
#c.DisplayAutoGrades.as_json = False

## Warning to display when a cell has changed.
#c.DisplayAutoGrades.changed_warning = "THE CONTENTS OF {num_changed} TEST CELL(S) HAVE CHANGED!\nThis might mean that even though the tests are passing\nnow, they won't pass when your assignment is graded.\n"

## Warning to display when a cell fails.
#c.DisplayAutoGrades.failed_warning = 'VALIDATION FAILED ON {num_failed} CELL(S)! If you submit\nyour assignment as it is, you WILL NOT receive full\ncredit.\n'

## Don't complain if cell checksums have changed (if they are locked cells) or
#  haven't changed (if they are solution cells)
#c.DisplayAutoGrades.ignore_checksums = False

## A string containing whitespace that will be used to indent code and errors
#c.DisplayAutoGrades.indent = '    '

## Complain when cells pass, rather than fail.
#c.DisplayAutoGrades.invert = False

## Warning to display when a cell passes (when invert=True)
#c.DisplayAutoGrades.passed_warning = 'NOTEBOOK PASSED ON {num_passed} CELL(S)!\n'

## Maximum line width for displaying code/errors
#c.DisplayAutoGrades.width = 90

#------------------------------------------------------------------------------
# ComputeChecksums(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor to compute checksums of grade cells.

#------------------------------------------------------------------------------
# SaveCells(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor to save information about grade and solution cells.

#------------------------------------------------------------------------------
# OverwriteCells(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor to overwrite information about grade and solution cells.

#------------------------------------------------------------------------------
# CheckCellMetadata(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor for checking that grade ids are unique.

#------------------------------------------------------------------------------
# ExecutePreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------

## Executes all the cells in a notebook

## If `False` (default), when a cell raises an error the execution is stopped and
#  a `CellExecutionError` is raised. If `True`, execution errors are ignored and
#  the execution is continued until the end of the notebook. Output from
#  exceptions is included in the cell output in both cases.
#c.ExecutePreprocessor.allow_errors = False

## If execution of a cell times out, interrupt the kernel and continue executing
#  other cells rather than throwing an error and stopping.
#c.ExecutePreprocessor.interrupt_on_timeout = False

## The time to wait (in seconds) for IOPub output. This generally doesn't need to
#  be set, but on some slow networks (such as CI systems) the default timeout
#  might not be long enough to get all messages.
#c.ExecutePreprocessor.iopub_timeout = 4

## The kernel manager class to use.
#c.ExecutePreprocessor.kernel_manager_class = 'jupyter_client.manager.KernelManager'

## Name of kernel to use to execute the cells. If not set, use the kernel_spec
#  embedded in the notebook.
#c.ExecutePreprocessor.kernel_name = ''

## If `False` (default), then the kernel will continue waiting for iopub messages
#  until it receives a kernel idle message, or until a timeout occurs, at which
#  point the currently executing cell will be skipped. If `True`, then an error
#  will be raised after the first timeout. This option generally does not need to
#  be used, but may be useful in contexts where there is the possibility of
#  executing notebooks with memory-consuming infinite loops.
#c.ExecutePreprocessor.raise_on_iopub_timeout = False

## If `graceful` (default), then the kernel is given time to clean up after
#  executing all cells, e.g., to execute its `atexit` hooks. If `immediate`, then
#  the kernel is signaled to immediately terminate.
#c.ExecutePreprocessor.shutdown_kernel = 'graceful'

## The time to wait (in seconds) for output from executions. If a cell execution
#  takes longer, an exception (TimeoutError on python 3+, RuntimeError on python
#  2) is raised.
#  
#  `None` or `-1` will disable the timeout. If `timeout_func` is set, it
#  overrides `timeout`.
#c.ExecutePreprocessor.timeout = 30

## A callable which, when given the cell source as input, returns the time to
#  wait (in seconds) for output from cell executions. If a cell execution takes
#  longer, an exception (TimeoutError on python 3+, RuntimeError on python 2) is
#  raised.
#  
#  Returning `None` or `-1` will disable the timeout for the cell. Not setting
#  `timeout_func` will cause the preprocessor to default to using the `timeout`
#  trait for all cells. The `timeout_func` trait overrides `timeout` if it is not
#  `None`.
#c.ExecutePreprocessor.timeout_func = None

#------------------------------------------------------------------------------
# Execute(NbGraderPreprocessor,ExecutePreprocessor) configuration
#------------------------------------------------------------------------------

## The number of times to try re-executing the notebook before throwing an error.
#  Generally, this shouldn't need to be set, but might be useful for CI
#  environments when tests are flaky.
#c.Execute.execute_retries = 0

## A list of extra arguments to pass to the kernel. For python kernels, this
#  defaults to ``--HistoryManager.hist_file=:memory:``. For other kernels this is
#  just an empty list.
#c.Execute.extra_arguments = []

#------------------------------------------------------------------------------
# GetGrades(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## Preprocessor for saving grades from the database to the notebook

## 
#c.GetGrades.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

#------------------------------------------------------------------------------
# ClearOutputPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------

## Removes the output from all code cells in a notebook.

#------------------------------------------------------------------------------
# ClearOutput(NbGraderPreprocessor,ClearOutputPreprocessor) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# LimitOutput(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## Preprocessor for limiting cell output

## maximum number of lines of output (-1 means no limit)
#c.LimitOutput.max_lines = 1000

## maximum number of traceback lines (-1 means no limit)
#c.LimitOutput.max_traceback = 100

#------------------------------------------------------------------------------
# DeduplicateIds(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor to overwrite information about grade and solution cells.
