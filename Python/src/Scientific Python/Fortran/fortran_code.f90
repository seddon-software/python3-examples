program simple
    implicit none
    integer :: y,z
    integer, external :: square

    y = 20
    z = square(y)
    print *, "z = ",z
end program

integer function square(x)
    implicit none
    integer, intent(in) :: x
    square = x**2
end function
