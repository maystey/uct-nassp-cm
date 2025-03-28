# Uncertainty in Numerical Methods

In this chapter the measurement uncertainty framework outlined in the Guide to the expression of uncertainty in measurement is introduced. This will be adapted to the numerical methods covered in this course more directly in each of the chapters dedicated to the numerical methods.

In this chapter works from the Joint Committee for Guides in Metrology (JCGM) are used, specifically:

- "Guide to the expression of uncertainty in measurement" (GUM) {cite}`u-i-JCGMGUM`
- "International vocabulary of metrology" (VIM) {cite}`u-i-JCGMVIM3`
- Additional GUM supplements  <!-- %TODO cite ones used -->

<!-- Metrology is the science of measurement (normally physical) - terminology will reflect this -->

\begin{frame}{What is a measurement?}
\begin{itemize}
    \item The objective of a measurement: determine the unique value of a physical quantity - the \textbf{measurand}.
    % \item Realistically, we cannot know the ``true value'' of the measurand, instead we determine an interval of likely values, along with a level of confidence for this interval
    \item Cannot know value of measurand with absolute certainty
    \begin{itemize}
        \item Limited definition
        \item Limited by nature of measurement (apparatus, etc)
    \end{itemize}

    % \item Determined by the nature of the measurement, and the apparatus involved
    \item Usually quoted as a best approximation %/ central value 
    of the measurand, along with an \textbf{uncertainty of the measurement} %or uncertainty of measurement?
    \item \textbf{Standard uncertainty} - uncertainty of a measurement expressed as a standard deviation.
    %  that can be used to determine the interval of likely values around this
    \item \textbf{Note} some people use \textbf{error} interchangeably with \textbf{uncertainty}.
    \begin{itemize}
        \item I will use the term \textbf{uncertainty} precisely as described in the GUM. 
        \item I will use the term \textbf{error} in more general cases:
        \begin{itemize}
            \item Errors as flaws in code
            \item Errors as resulting from approximations in numerical methods
        \end{itemize}
    \end{itemize}
\end{itemize}
\end{frame}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{frame}{Uncertainty of a Measurement}
From the GUM \autocite{JCGMGUM} and VIM \autocite{JCGMVIM3}:

\begin{itemize}
    \item parameter, associated with the result of a measurement, that characterizes the dispersion of the values that
    could reasonably be attributed to the measurand.
\end{itemize}

\end{frame}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{frame}{Sources of Uncertainty}

%Mention QM's inherent probabilistic nature?
\begin{block}{Physical Measurements}
    \begin{itemize}
        \item Precision of measurement instruments
        \item Randomness due to uncontrollable complexities in a physical system
    \end{itemize}
\end{block}

\begin{block}{Numerical Algorithms}
    \begin{itemize}
        \item Floating point precision (often negligible)
        \item Truncation errors (from specific algorithm used)
        \item Randomness from sampling random variables
    \end{itemize}
\end{block}

\end{frame}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{frame}{Important Terminology for Uncertainty}{Methods of Uncertainty Evaluation}

    \begin{itemize}
        \item Knowledge of the distribution of possible measurand values is needed to determine the uncertainty of a measurement
        \begin{itemize}
            \item Often in the form of a \textbf{probability distribution function} (PDF).
        \end{itemize}
        \item There are two types of methodologies for evaluating the uncertainty of a measurement result defined in GUM\autocite{JCGMGUM}:
    \end{itemize}
    % Knowledge of the distribution of possible measurand values is needed to determine the uncertainty of a measurement, which is often in the form of a \textbf{probability distribution function} (PDF).
    
    \begin{block}{Type A evaluation of uncertainty}
        Evaluating uncertainty by \textbf{statistical analysis} of a series of observations - PDF derived from observed frequency distribution
    \end{block}
    
    \begin{block}{Type B evaluation of uncertainty}
        Evaluation of uncertainty by other means (includes single measurements) -  PDF assumed based on knowledge of measurement
    \end{block}
    
\end{frame}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{frame}{Mathematical Notation}
    \begin{itemize}
        \item Given a measurand $X$, an estimation of this (as resulting from a measurement) is denoted as $x$. 
        \item The standard uncertainty of this estimation will be denoted by $u(x)$.
        \item Note that $u(x)$ should not be interpreted as a function of $x$.
    \end{itemize}
    
\end{frame}


## References
```{bibliography}
:cited:
:style: plain
:labelprefix: U
:keyprefix: u-i-
```