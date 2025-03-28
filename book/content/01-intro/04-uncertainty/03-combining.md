\begin{frame}{Combined Standard Uncertianties}{Terminology}
    
\begin{itemize}
    \item Sometimes a measurand is determined by combining multiple measurements.
\end{itemize}

    \begin{block}{Combined standard uncertainty}
        The standard uncertainty of the result of a measurement, where this result was acquired by combining a number of other quantities with standard uncertainties. These standard uncertainties are generally combined in quadrature.

        The framework that GUM provides for combining uncertainties makes it particularly useful.
    \end{block}
\end{frame}


\begin{frame}{Combined / Propogating Standard Uncertainties}{Uncorrelated Quantities}
    \begin{itemize}
        \item Measurand $Y$ obtained by combining \textbf{uncorrelated / independent} measurands $X_1, \dots, X_N$:
        
        \begin{equation*}
            Y = f(X_1, \dots, X_N)
        \end{equation*}

        \item The combined variance of $y$ is given by:
        
        \begin{equation*}
            u^2(y) = \sum_{i=1}^N \left( \frac{\partial f}{\partial x_i} \right)^2 u^2 (x_i)
        \end{equation*}

        where $\tfrac{\partial f}{\partial x_i}$ represents $\tfrac{\partial f}{\partial X_i}$ at $X_i = x_i$.

        \item The equation above is derived from the Taylor expansion of $f$.
    \end{itemize}
\end{frame}

%TODO: Introduce correlation term as a way of testing this
\begin{frame}{Combined / Propogating Standard Uncertainties}{Correlated Quantities}
    \begin{itemize}
        \item If the $X_i$ are correlated / dependant, then:
        
        \begin{align*}
            u^2(y) & = \sum_{i=1}^N \sum_{j = 1}^N \frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j} u(x_i, x_j) \\
            & = \sum_{i=1}^N \left( \frac{\partial f}{\partial x_i} \right)^2 u^2 (x_i) + 2 \sum_{i=1}^{N-1}\sum_{j=i+1}^{N} \frac{\partial f}{\partial x_i}\frac{\partial f}{\partial x_j} u(x_i, x_j)\\
        \end{align*}

        where $u(x_i, x_j)$ is the covariance between $x_i$ and $x_j$.
        % \item To check if two measurements are correlated, you can use the 
    \end{itemize}
\end{frame}