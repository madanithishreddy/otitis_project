export const metadata = {
  title: "Dashboard | OtoScopeAI | A Healthcare App",
};

import React from "react";

import { cookies, headers } from "next/headers";
import axios from "axios";
import Layout from "./components/Layout";
import Overview from "./components/Overview";

async function getData() {
  const cookieStore = cookies();
  const access = cookieStore.get("access");
  const userConfig = {
    headers: {
      Authorization: "Bearer " + access?.value,
    },
  };

  try {
    const { data } = await axios.get(
      process.env.API_URL + "/api/v1/analytics/",
      userConfig
    );

    if (!data) {
      throw new Error("No data received from the server");
    }

    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error fetching data:", {
        status: error.response?.status,
        headers: error.response?.headers,
        data: error.response?.data,
      });
      throw new Error(
        "Failed to fetch data: " +
          (error.response?.data?.message || error.message)
      );
    } else {
      console.error("Unexpected error fetching data:", error);
      throw new Error("Failed to fetch data: " + String(error));
    }
  }
}

export default async function Dashboard() {
  const data = await getData();
  return (
    <div className="flex flex-col items-center top-0 min-h-screen">
      <Layout title="Dashboard">
        <main className="max-w-7xl container mx-auto px-8 sm:px-14 lg:px-20 w-full min-h-[75vh]">
          <Overview data={data} />
          {/* <Activity /> */}
          {/* <Patients data={data} /> */}
        </main>
      </Layout>
    </div>
  );
}
