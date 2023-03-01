PROGRAM clv_init

    INTEGER, PARAMETER :: JPIM = SELECTED_INT_KIND(9)
    INTEGER, PARAMETER :: JPRB = SELECTED_REAL_KIND(13, 300)

    ! Why are these set here again?
    INTEGER(KIND=JPIM), PARAMETER  :: KLON = 100
    INTEGER(KIND=JPIM), PARAMETER  :: KLEV = 100
    INTEGER(KIND=JPIM), PARAMETER  :: NCLV = 100

    INTEGER(KIND=JPIM) KIDIA 
    INTEGER(KIND=JPIM) KFDIA 

    REAL(KIND=JPRB) PCLV(KLON,KLEV,NCLV)
    REAL(KIND=JPRB) PTSPHY
    ! tendency_tmp was originally a class where the different attribute cld was used
    REAL(KIND=JPRB) tendency_tmp_cld(KLON,KLEV,NCLV)


    REAL(KIND=JPRB) ZQX(KLON,KLEV,NCLV) 
    REAL(KIND=JPRB) ZQX0(KLON,KLEV,NCLV) 

    CALL clv_init_routine(&
    & KLON, KLEV, NCLV, KIDIA, KFDIA, PCLV, PTSPHY, tendency_tmp_cld, ZQX, ZQX0)

END PROGRAM

SUBROUTINE clv_init_routine(&
    & KLON, KLEV, NCLV, KIDIA, KFDIA, PCLV, PTSPHY, tendency_tmp_cld, ZQX, ZQX0)

    INTEGER, PARAMETER :: JPIM = SELECTED_INT_KIND(9)
    INTEGER, PARAMETER :: JPRB = SELECTED_REAL_KIND(13, 300)

    INTEGER(KIND=JPIM) KLON
    INTEGER(KIND=JPIM) KLEV
    INTEGER(KIND=JPIM) NCLV
    INTEGER(KIND=JPIM) KIDIA 
    INTEGER(KIND=JPIM) KFDIA 

    REAL(KIND=JPRB) PCLV(KLON,KLEV,NCLV)
    REAL(KIND=JPRB) PTSPHY
    ! tendency_tmp was originally a class where the different attribute cld was used
    REAL(KIND=JPRB) tendency_tmp_cld(KLON,KLEV,NCLV)


    REAL(KIND=JPRB) ZQX(KLON,KLEV,NCLV) 
    REAL(KIND=JPRB) ZQX0(KLON,KLEV,NCLV) 

    DO JM=1,NCLV-1
        DO JK=1,KLEV
            DO JL=KIDIA,KFDIA
                ZQX(JL,JK,JM)  = PCLV(JL,JK,JM)+PTSPHY*tendency_tmp_cld(JL,JK,JM)
                ZQX0(JL,JK,JM) = PCLV(JL,JK,JM)+PTSPHY*tendency_tmp_cld(JL,JK,JM)
            ENDDO
        ENDDO
    ENDDO
END SUBROUTINE
