\begin{frame}{Expanded Uncertainty}{Terminology}

\begin{block}{Expanded uncertainty}
    A ``quantity defining an interval about the result of a measurement that may be expected to encompass a large [coverage probability / level of confidence] of the distribution of values that could reasonably be attributed to the measurand''\autocite{JCGMGUM}.
\end{block}

\begin{block}{Coverage factor}
    A ``numerical factor [typically in the range of 2 to 3] used as a multiplier of the combined standard uncertainty in order to obtain an expanded
    uncertainty''\autocite{JCGMGUM}.
\end{block}

\end{frame}

\begin{frame}{Expanded Uncertainty}
    \begin{itemize}
        \item Want to use our uncertainty to create an interval, in which we have a specified level of confidence:
        
        \begin{equation*}
            Y = y \pm k u(y)
        \end{equation*}

        where $k$ is the ``coverage factor''.
        \item Determining $k$ for the required level of confidence $p$ is not so straight forward.
        \item Following a normal distribution this can be approximated as:
        \begin{itemize}
            \item $p = 68\%$ for $k = 1$
            \item  $p = 95\%$ for $k = 2$
            \item $p = 99\%$ for $k = 3$
        \end{itemize}

    \end{itemize}
\end{frame}