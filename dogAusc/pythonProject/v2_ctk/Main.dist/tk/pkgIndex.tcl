<<<<<<< HEAD
if {![package vsatisfies [package provide Tcl] 8.6.0]} return
package ifneeded Tk 8.6.14 [list load [file normalize [file join $dir .. libtk8.6.dylib]]]
=======
if {![package vsatisfies [package provide Tcl] 8.6.0]} return
if {($::tcl_platform(platform) eq "unix") && ([info exists ::env(DISPLAY)]
	|| ([info exists ::argv] && ("-display" in $::argv)))} {
    package ifneeded Tk 8.6.13 [list load [file join $dir .. .. bin libtk8.6.dll]]
} else {
    package ifneeded Tk 8.6.13 [list load [file join $dir .. .. bin tk86t.dll]]
}
>>>>>>> 8fe14cb1b0cd0cbfa811d5ededcb79ce4bddb09e
