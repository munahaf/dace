PROGRAM non_clv_init
    INTEGER, PARAMETER :: JPIM = SELECTED_INT_KIND(9)
    INTEGER, PARAMETER :: JPRB = SELECTED_REAL_KIND(13, 300)

    ! Why are these set here again?
    INTEGER(KIND=JPIM), PARAMETER  :: KLON = 100
    INTEGER(KIND=JPIM), PARAMETER  :: KLEV = 100
    INTEGER(KIND=JPIM), PARAMETER  :: NCLV = 100

    INTEGER(KIND=JPIM) KIDIA 
    INTEGER(KIND=JPIM) KFDIA 
    INTEGER(KIND=JPIM) NCLDQV 

    REAL(KIND=JPRB) PTSPHY
    ! tendency_tmp was originally a class where the different attributes t, q and a were used
    REAL(KIND=JPRB) tendency_tmp_t(KLON,KLEV)
    REAL(KIND=JPRB) tendency_tmp_q(KLON,KLEV)
    REAL(KIND=JPRB) tendency_tmp_a(KLON,KLEV)
    REAL(KIND=JPRB) ZTP1(KLON,KLEV)
    REAL(KIND=JPRB) PT(KLON,KLEV)
    REAL(KIND=JPRB) PQ(KLON,KLEV)
    REAL(KIND=JPRB) PA(KLON,KLEV)

    REAL(KIND=JPRB) ZQX(KLON,KLEV,NCLV) 
    REAL(KIND=JPRB) ZQX0(KLON,KLEV,NCLV) 
    REAL(KIND=JPRB) ZA(KLON,KLEV)
    REAL(KIND=JPRB) ZAORIG(KLON,KLEV)

    CALL non_clv_init_routine( &
    & KLON, KLEV, NCLV, KIDIA, KFDIA, NCLDQV, &
    & PTSPHY, tendency_tmp_t, tendency_tmp_q, tendency_tmp_a, PT, PQ, PA, ZTP1, ZQX, ZQX0, ZA, ZAORIG)

END

SUBROUTINE non_clv_init_routine( &
    & KLON, KLEV, NCLV, KIDIA, KFDIA, NCLDQV, &
    & PTSPHY, tendency_tmp_t, tendency_tmp_q, tendency_tmp_a, ZTP1, ZQX, ZQX0, ZA, ZAORIG, PT, PQ, PA)

    INTEGER, PARAMETER :: JPIM = SELECTED_INT_KIND(9)
    INTEGER, PARAMETER :: JPRB = SELECTED_REAL_KIND(13, 300)

    INTEGER(KIND=JPIM) KLON
    INTEGER(KIND=JPIM) KLEV
    INTEGER(KIND=JPIM) NCLV
    INTEGER(KIND=JPIM) KIDIA 
    INTEGER(KIND=JPIM) KFDIA 
    INTEGER(KIND=JPIM) NCLDQV 

    REAL(KIND=JPRB) PTSPHY
    ! tendency_tmp was originally a class where the different attributes t, q and a were used
    REAL(KIND=JPRB) tendency_tmp_t(KLON,KLEV)
    REAL(KIND=JPRB) tendency_tmp_q(KLON,KLEV)
    REAL(KIND=JPRB) tendency_tmp_a(KLON,KLEV)
    REAL(KIND=JPRB) PT(KLON,KLEV)
    REAL(KIND=JPRB) PQ(KLON,KLEV)
    REAL(KIND=JPRB) PA(KLON,KLEV)

    REAL(KIND=JPRB) ZTP1(KLON,KLEV)
    REAL(KIND=JPRB) ZQX(KLON,KLEV,NCLV) 
    REAL(KIND=JPRB) ZQX0(KLON,KLEV,NCLV) 
    REAL(KIND=JPRB) ZA(KLON,KLEV)
    REAL(KIND=JPRB) ZAORIG(KLON,KLEV)

 
    DO JK=1,KLEV        ! LOOP CLASS 1
        DO JL=KIDIA,KFDIA
            ZTP1(JL,JK)        = PT(JL,JK)+PTSPHY*tendency_tmp_t(JL,JK)
            ZQX(JL,JK,NCLDQV)  = PQ(JL,JK)+PTSPHY*tendency_tmp_q(JL,JK) 
            ZQX0(JL,JK,NCLDQV) = PQ(JL,JK)+PTSPHY*tendency_tmp_q(JL,JK)
            ZA(JL,JK)          = PA(JL,JK)+PTSPHY*tendency_tmp_a(JL,JK)
            ZAORIG(JL,JK)      = PA(JL,JK)+PTSPHY*tendency_tmp_a(JL,JK)
        ENDDO
    ENDDO

END SUBROUTINE
 
