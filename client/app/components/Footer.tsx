import { urls } from "@/lib/urls";
import Image from "next/image";
import Link from "next/link";

export function Footer({ locale }: { locale: Locale }) {
  return (
    <footer className="border-t-1 border-t-night mt-auto border-dashed">
      <div className="mx-auto max-w-7xl py-3">
        <ul className="align-center my-3 flex-wrap justify-between text-center sm:flex">
          <li className="mx-2">
            <Link className="text-night" href="#">
              Feed
            </Link>
          </li>
          <li className="mx-2">
            <Link className="text-night" href={urls(locale).github}>
              GitHub
            </Link>
          </li>
        </ul>
        <div className="flex flex-col sm:flex-row">
          <Link
            className="mx-auto my-auto flex-shrink-0"
            rel="license"
            href="http://creativecommons.org/licenses/by-sa/4.0/"
          >
            <Image
              alt="Creative Commons License"
              src="/img/cc-4-0-by-sa.png"
              width={88}
              height={31}
            />
          </Link>
          <span className="block text-center sm:ml-4 sm:inline sm:text-left">
            Satoshi Nakamoto Institute is licensed under a{" "}
            <Link
              rel="license"
              href="http://creativecommons.org/licenses/by-sa/4.0/"
            >
              Creative Commons Attribution-ShareAlike 4.0 International License
            </Link>
            . Some works may be subject to other licenses.
          </span>
        </div>
      </div>
    </footer>
  );
}
